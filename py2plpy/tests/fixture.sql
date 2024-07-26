CREATE OR REPLACE FUNCTION f (
    IN a TEXT,
    b INTEGER,
    c DOUBLE PRECISION,
    d BOOLEAN,
    e BYTEA,
    f NUMERIC,
    g SMALLINT,
    h BIGINT,
    INOUT i REAL,
    OUT j DOUBLE PRECISION)
    RETURNS SETOF RECORD
    STRICT
    VOLATILE
    PARALLEL RESTRICTED
    LEAKPROOF
    SECURITY INVOKER
    COST 1000
    ROWS 5
    SUPPORT support.func
    SET work_mem = '4MB'
    SET hash_mem_multiplier = '1.0'
    TRANSFORM FOR TYPE jsonb
    LANGUAGE PLPYTHON3U
    AS $BODY$
    
    
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
    $BODY$;
    
    