from decimal import Decimal
from typing import List
from py2plpy import sql_properties, In, Out, InOut, SmallInt, BigInt, Real, Double, SetOf, Record, plpy

class jsonb:
    pass

@sql_properties(
        strict = True, 
        volatility = 'volatile', 
        parallel = 'restricted', 
        leakproof = True, 
        security = 'invoker',
        cost = 1000,
        rows = 5,
        support = 'support.func',
        set =  [('work_mem', '4MB'), ('hash_mem_multiplier', '1.0')],
        transform = [jsonb],
        procedure = False
    )
def f(
        a: In[str], 
        b: int, 
        c: float, 
        d: bool, 
        e: bytes, 
        f: Decimal, 
        g: SmallInt, 
        h: BigInt, 
        i: InOut[Real], 
        j: Out[Double]
    ) -> SetOf[Record]:

    import re

    
    plpy.debug(
        'foo', 
        'bar', 
        detail = 'detail', 
        hint = 'hint',
        sqlstate = '01000',
        schema_name = 'schema_name',
        table_name = 'table_name',
        column_name = 'column_name',
        datatype_name = 'datatype_name', 
        constraint_name = 'constraint_name')
    plpy.log(
        'foo', 
        'bar', 
        detail = 'detail', 
        hint = 'hint',
        sqlstate = '01000',
        schema_name = 'schema_name',
        table_name = 'table_name',
        column_name = 'column_name',
        datatype_name = 'datatype_name', 
        constraint_name = 'constraint_name')
    plpy.info(
        'foo', 
        'bar', 
        detail = 'detail', 
        hint = 'hint',
        sqlstate = '01000',
        schema_name = 'schema_name',
        table_name = 'table_name',
        column_name = 'column_name',
        datatype_name = 'datatype_name', 
        constraint_name = 'constraint_name')
    plpy.warning(
        'foo', 
        'bar', 
        detail = 'detail', 
        hint = 'hint',
        sqlstate = '01000',
        schema_name = 'schema_name',
        table_name = 'table_name',
        column_name = 'column_name',
        datatype_name = 'datatype_name', 
        constraint_name = 'constraint_name')
    plpy.error(
        'foo', 
        'bar', 
        detail = 'detail', 
        hint = 'hint',
        sqlstate = '01000',
        schema_name = 'schema_name',
        table_name = 'table_name',
        column_name = 'column_name',
        datatype_name = 'datatype_name', 
        constraint_name = 'constraint_name')
    plpy.fatal(
        'foo', 
        'bar', 
        detail = 'detail', 
        hint = 'hint',
        sqlstate = '01000',
        schema_name = 'schema_name',
        table_name = 'table_name',
        column_name = 'column_name',
        datatype_name = 'datatype_name', 
        constraint_name = 'constraint_name')
    
    plan = plpy.prepare('SELECT * FROM t WHERE id = $', ['integer'])
    rv = plpy.execute(plan, [5], 5)
    nrows: int = rv.nrows()
    status: int = rv.status()
    colnames: List[str] = rv.colnames()
    coltypes: List[str] = rv.coltypes()
    coltypmods:  List[str] = rv.coltypmods()


    with plpy.subtransaction():
        for row in plpy.cursor(plan, [5]):
            plpy.info(row['a'])


    for i, m in enumerate(re.findall(r'x', a)):
        yield i, m