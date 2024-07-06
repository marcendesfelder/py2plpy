# py2plpy

pl2ply is a simple python package that makes it easy to write PostgreSQL PL/Python functions as native python code and then convert them to SQL. 

It consits of five elements:
- a `transform` function that reads a python file and returns PL/Python code for all functions at the root of the file
- a `sql_properties` decorator that adds SQL-specific information to a python function
- predefined types `Out`, `In`, `InOut`, `SetOf` and `Record`
- a dummy `plpy` object that mimics the corresponding Pl/Python object
- the `pl2plpy`command line tool

## Usage

```python
# fruit.py

from py2plpy import sql_properties, Out, SetOf, Record, plpy

@sql_properties(strict=True)
def find_fruit(string:str, fruit_no:Out[int], fruit:Out[str]) -> SetOf[Record]:
    import re
    
    plpy.info('Searching for fruit...')
    for i, m in enumerate(re.findall(r'apple|pear|banana', string)):
        yield i, m
```

```
py2plpy fruit.py fruit.sql
```

```sql
-- fruit.sql

CREATE OR REPLACE FUNCTION find_fruit (
    string TEXT,
    OUT fruit_no INTEGER,
    OUT fruit TEXT)
    RETURNS SETOF RECORD
    STRICT
    LANGUAGE PLPYTHON3U
    AS $BODY$
    
        import re
        
        plpy.info('Searching for fruit...')
        for i, m in enumerate(re.findall(r'apple|pear|banana', string)):
            yield i, m
    $BODY$;
```