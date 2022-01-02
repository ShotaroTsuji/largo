import os
from typing import Optional, Tuple, Union

__version__ = '0.1.0'

PathLike = Union[str, os.PathLike[str]]


class Month:
    month_strings = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',
                     'sep', 'oct', 'nov', 'dec']

    def __init__(self, s: str) -> None:
        self._month = self.month_strings.index(s) + 1

    def __int__(self) -> int:
        return self._month

    def __str__(self) -> str:
        return self.month_strings[self._month - 1]

    def __next__(self):
        if self._month == 12:
            raise StopIteration()

        month = Month('jan')
        month._month = self._month + 1
        return month

    def to_range_str(self) -> Tuple[str, Optional[str]]:
        if self._month == 12:
            return (str(self), None)
        else:
            return (str(self), str(next(self)))


