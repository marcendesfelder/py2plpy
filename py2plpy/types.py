import sys
from typing import Iterator, TypeVar

if sys.version_info < (3, 12, 0):
    from typing_extensions import TypeAliasType
else:
    from typing import TypeAliasType

T = TypeVar('T')
Out = TypeAliasType('Out', T, type_params = (T,))
In = TypeAliasType('In', T, type_params = (T,))
InOut = TypeAliasType('InOut', T, type_params = (T,))
SetOf = TypeAliasType('SetOf', Iterator[T], type_params = (T,))
Record = TypeAliasType('RECORD', any)
SmallInt = TypeAliasType('SMALLINT', int)
BigInt = TypeAliasType('BIGINT', int)
Real = TypeAliasType('REAL', float)
Double = TypeAliasType('DOUBLE PRECISION', float)