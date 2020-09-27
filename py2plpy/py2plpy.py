import inspect
import os
import sys
import importlib
import re
from lark import Lark

l = Lark.open('py2plpy/grammar.lark')

p = '''CREATE OR REPLACE FUNCTION {schema}.{name} (
{arguments})
RETURNS {returntype}
LANGUAGE 'plpython3u' 
{properties}
AS $BODY$
{body}
$BODY$;'''


types = {
    int : 'INTEGER',
    str : 'TEXT',
    float : 'DOUBLE',
    bool : 'BOOLEAN'
}

def convertType(t):
    try:
        return types[t]
    except KeyError:
        pass
    try:
        if t.__origin__ == list:
            return types[t.__args__[0]]+'[]'
    except:
        return str(t)

def getBody(f):
    body = re.sub(r'^([^\n\(]|\([^\)]*\))+\n', '', inspect.getsource(f)).rstrip()
    s = re.match(r'^ *[ruRU]?(\'\'\'|"""|\'|")', body)
    if s:
        i = body[s.end():].find(s.group(1)) + s.end() + len(s.group(1))
        body = '    '+body[i:].lstrip()
    return body


def parseDoc(f):
        tree = l.parse(inspect.getdoc(f).upper())
        properties = {}
        for s in tree.iter_subtrees():
            if s.data == 'strict':
                properties['strictness'] = 'STRICT'
            elif s.data == 'nonstrict':
                properties['strictness'] = 'CALLED ON NULL INPUT'
            elif s.data == 'volatile':
                properties['volatility'] = 'VOLATILE'
            elif s.data == 'immutable':
                properties['volatility'] = 'IMMUTABLE'
            elif s.data == 'stable':
                properties['volatility'] = 'STABLE'
            elif s.data == 'parasafe':
                properties['parallelism'] = 'PARALLEL SAFE'
            elif s.data == 'paraunsafe':
                properties['parallelism'] = 'PARALLEL UNSAFE'
            elif s.data == 'pararestricted':
                properties['parallelism'] = 'PARALLEL RESTRICTED'
            elif s.data == 'invoker':
                properties['security'] = 'EXTERNAL SECURITY INVOKER'
            elif s.data == 'definer':
                properties['security'] = 'EXTERNAL SECURITY DEFINER'
            elif s.data == 'leakproof':
                properties['leakiness'] == 'LEAKPROOF'
            elif s.data == 'nonleakproof':
                properties['leakiness'] == 'NOT LEAKPROOF'
            elif s.data == 'cost':
                properties['cost'] = 'COST '+s.children[0]
            elif s.data == 'rows':
                properties['rows'] = 'ROWS '+s.children[0]
        return '\n'.join(properties.values())


def transformFunc(f, schema = 'public'):
    d = {}
    s = inspect.signature(f)
    d['arguments'] = ',\n'.join([param.name+' '+convertType(param.annotation) for param in s.parameters.values()])
    d['returntype'] = convertType(s.return_annotation)
    d['body'] = getBody(f)
    d['name'] = f.__name__
    d['properties'] = parseDoc(f)
    d['schema'] = schema
    return p.format_map(d) 
    

def transform(path):
    d, file = os.path.split(path)
    sys.path.insert(1, d)
    name = os.path.splitext(file)[0]
    m = importlib.import_module(name)

    res = ''
    for _, obj in inspect.getmembers(m, inspect.isroutine):
        res += transformFunc(obj)

    return res.replace('\n', '\n    ')