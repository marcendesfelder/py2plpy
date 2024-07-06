import inspect
import os
import sys
import importlib
import re
from typing import Generic, TypeVar, List
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Modifier:
    def __init__(self, type):
        self.type = type

T = TypeVar('T')
class Out(Generic[T], Modifier):
    pass
class In(Generic[T], Modifier):
    pass
class InOut(Generic[T], Modifier):
    pass
class SetOf(Generic[T], Modifier):
    pass

class Record:
    pass


p = '''CREATE OR REPLACE {routine} {schema}{name} (
{arguments})
{properties}
AS $BODY$
{body}
$BODY$;'''

types = {
    int: 'INTEGER',
    str: 'TEXT',
    float: 'DOUBLE',
    bool: 'BOOLEAN',
    Record: 'RECORD'
}


def convertType_(t):
    if t in types:
        return types[t]
    if hasattr(t, '__origin__') and t.__origin__ == list:
        return convertType_(t.__args__[0])+'[]'
    return t.__name__


def convertType(t):
    if hasattr(t, '__origin__'):
        if t.__origin__ == Out:
            return convertType_(t.__args__[0]), 'OUT '
        elif t.__origin__ == In:
            return convertType_(t.__args__[0]), 'IN '
        elif t.__origin__ == InOut:
            return convertType_(t.__args__[0]), 'INOUT '
        elif t.__origin__ == SetOf:
            return convertType_(t.__args__[0]), 'SETOF '
    return convertType_(t), ''

def param(name, t):
    type, prefix = convertType(t)
    return prefix + name + ' ' + type

def returntype(t):
    type, prefix = convertType(t)
    return prefix + type


def getBody(f):
    body = inspect.getsource(f)
    level = 0
    i = 0
    for c in body:
        if c == ':' and level == 0:
            break
        elif c == '(':
            level += 1
        elif c == ')':
            level -= 1
        i += 1
    body = body[i+1:].rstrip()

    s = re.match(r'^ *[ruRU]?(\'\'\'|"""|\'|")', body)
    if s:
        i = body[s.end():].find(s.group(1)) + s.end() + len(s.group(1))
        body = '    '+body[i:].lstrip()
    return body


def sql_properties(
        strict:bool = False, 
        volatility:Literal['volatile', 'stable', 'immutable'] = None, 
        parallel:Literal['safe', 'unsafe', 'restricted'] = None, 
        leakproof:bool = None, 
        cost:int = None,
        rows:int = None,
        transform:List[type]=[],
        procedure:bool = False):
    properties = []
    if strict == True:
        properties.append('STRICT')
    elif strict == False and not procedure:
        properties.append('CALLED ON NULL INPUT')
    if volatility:
        properties.append(volatility.upper())
    if parallel:
        properties.append(parallel.upper())
    if leakproof == True:
        properties.append('LEAKPROOF')
    elif leakproof == False:
        properties.append('NOT LEAKPROOF')
    if cost is not None:
        properties.append(f'COST {cost}')
    if rows is not None:
        properties.append(f'ROWS {rows}')
    if transform:
        properties.append('TRANSFORM FOR TYPE '+', FOR TYPE '.join([convertType_(t) for t in transform]))

    def f(func):
        func._sqlProperties = properties
        func._sqlProcedure = procedure
        return func
    
    return f


def transformFunc(f, schema = None):
    d = {}
    s = inspect.signature(f)
    d['arguments'] = ',\n'.join([param(p.name, p.annotation) for p in s.parameters.values()])
    d['body'] = getBody(f)
    d['name'] = f.__name__
    properties = []
    if s.return_annotation != inspect.Signature.empty:
        properties.append('RETURNS ' + returntype(s.return_annotation))
    try:
        properties += f._sqlProperties
        d['routine'] = 'PROCEDURE' if f._sqlProcedure else 'FUNCTION'
    except AttributeError:
        d['routine'] = 'FUNCTION'
    d['properties'] = '\n'.join(properties+['LANGUAGE PLPYTHON3U'])
    d['schema'] = schema+'.' if schema is not None else ''
    return p.format_map(d) 
    

def transform(path):
    d, file = os.path.split(path)
    sys.path.insert(1, d)
    name = os.path.splitext(file)[0]
    m = importlib.import_module(name)

    res = ''
    for _, f in inspect.getmembers(m, inspect.isroutine):
        if f.__module__ == m.__name__:
            res += transformFunc(f) + '\n\n'

    return res.replace('\n', '\n    ')