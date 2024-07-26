# py2plpy

pl2ply is a simple python package that makes it easy to write PostgreSQL PL/Python functions as native python code with full tooling support. 

It consists of the following components:
- a `transform` function that reads a python file and returns PL/Python code for all functions at the root of the file
- a `sql_properties` decorator that adds SQL-specific information to a python function
- predefined type aliases `SmallInt`, `BigInt`, `Real`, `Double`, `Out`, `In`, `InOut`, `SetOf` and `Record`
- a dummy `plpy` object that implements the API of the corresponding Pl/Python object
- the `py2plpy`command line tool

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

## Custom Types

Any unknown type is represented by its `__name__` attribute in SQL. To use custom argument or return types, simply create a type of the appropriate name in Python. For full tooling support, it is usually most convienent to define it as an alias to type that will represent it in Python (typically `str`, `dict` for composite types):

```python
# from Python 3.12
type custom_type = str

# Python 3.11 and below
from typing_extensions import TypeAliasType
custom_type = TypeAliasType('custom_type', str)
```

## Missing Features

- Support for schema-qualified type names
- Predefined type aliases for PostgreSQL types with no native Python equivalent (e.g. `point`)