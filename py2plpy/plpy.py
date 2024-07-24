from typing import List, Union, Dict, Optional, Any

class QueryResult:
    def nrows(self) -> int:
        pass
    def status(self) -> int:
        pass
    def colnames(self) -> List[str]:
        pass
    def coltypes(self) -> List[str]:
        pass
    def coltypmods(self) -> List[str]:
        pass


class QueryPlan:
    pass


class CursorIterator:
    def __iter__(self) -> "CursorIterator":
        pass
    def __next__(self) -> Dict[str, Any]:
        pass


class Cursor:
    def fetch(self, count: int) -> QueryResult:
        pass
    def __iter__(self) -> "CursorIterator":
        pass


class Subtransaction:
    def __enter__(self) -> None:
        pass
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        pass


class Plpy:
    def __init__(self):
        pass
    def execute(self, queryOrPlan: Union[str, QueryPlan], argumentsOrLimit: Union[List[Any], int] = 0, limit: int = 0) -> QueryResult:
        pass
    def prepare(self, query: str, argtypes: List[str] = []) -> QueryPlan:
        pass
    def cursor(self, queryOrPlan: Union[str, QueryPlan], arguments: List[Any] = []) -> Cursor:
        pass

    def debug(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass
    def log(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass
    def info(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass
    def notice(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass
    def warning(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass
    def error(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass
    def fatal(
            self, 
            *msg: Any, 
            detail: Optional[str] = None, 
            hint: Optional[str] = None,
            sqlstate: Optional[str] = None,
            schema_name: Optional[str] = None,
            table_name: Optional[str] = None,
            column_name: Optional[str] = None,
            datatype_name: Optional[str] = None, 
            constraint_name: Optional[str] = None):
        pass

    def quote_literal(self, string:str) -> str:
        pass
    def quote_nullable(self, string:str) -> str:
        pass
    def quote_ident(self, string:str) -> str:
        pass
    
    def subtransaction(self) -> Subtransaction:
        pass
    def commit(self) -> None:
        pass
    def rollback(self) -> None:
        pass
    
    class SPIError:
        sqlstate: str

plpy = Plpy()