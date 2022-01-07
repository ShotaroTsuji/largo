import datetime
from attrs import define, field

def month_abbrevs() -> list[str]:
    return ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
            'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def month_to_abbrev(i: int) -> str:
    """
    Convert month number to month abbreviation.
    >>> month_to_abbrev(9)
    'sep'
    """
    return month_abbrevs()[i - 1]

def month_from_abbrev(s: str) -> int:
    """
    Convert month abbreviation to month number.
    >>> month_from_abbrev('jun')
    6
    """
    return month_abbrevs().index(s) + 1

class DateRange:
    def __init__(self, year, month=None) -> None:
        if month:
            if type(month) is str:
                month = month_from_abbrev(month)
                self._begin = datetime.date(year, month, 1)
                if month == 12:
                    self._end = datetime.date(year + 1, 1, 1)
                else:
                    self._end = datetime.date(year, month + 1, 1)
        else:
            self._begin = datetime.date(year, 1, 1)
            self._end = datetime.date(year + 1, 1, 1)

    @property
    def begin(self) -> datetime.date:
        return self._begin

    @property
    def end(self) -> datetime.date:
        return self._end


@define
class Year:
    """
    A class represents a year.
    >>> Year(2021)
    Year(year=2021)
    """
    year: int


@define
class Month:
    """
    A class represents a month.
    >>> Month('dec')
    Month(month=12)
    """
    month: int = field(converter = month_from_abbrev)


@define
class YearMonth:
    """
    A class represents year and month.
    >>> YearMonth(2021, 'dec')
    YearMonth(year=2021, month=12)
    """
    year: int
    month: int = field(converter = month_from_abbrev)
