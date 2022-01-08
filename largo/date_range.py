import datetime
import re
import typing
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
    """
    Represents a year/month period range.

    >>> period = DateRange(2021)
    >>> period.begin
    datetime.date(2021, 1, 1)
    >>> period.end
    datetime.date(2022, 1, 1)

    >>> period = DateRange(2021, 10)
    >>> period.begin
    datetime.date(2021, 10, 1)
    >>> period.end
    datetime.date(2021, 11, 1)
    """
    def __init__(self, year, month=None) -> None:
        if month:
            if type(month) is str:
                month = month_from_abbrev(month)
            elif type(month) is int:
                pass
            else:
                raise TypeError('`month` must be str or int')

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


def month_no_from_str_or_int(m: int | str) -> int:
    if type(m) is int:
        return m
    elif type(m) is str:
        return month_from_abbrev(m)
    else:
        raise TypeError('month must be int or str')


@define
class YearMonth:
    """
    A class represents year and month.

    >>> YearMonth(2021, 'dec')
    YearMonth(year=2021, month=12)
    >>> YearMonth(2021, 10)
    YearMonth(year=2021, month=10)
    """
    year: int
    month: int = field(converter = month_no_from_str_or_int)


def parse_date_argument(s: str) -> Year | Month | YearMonth:
    """
    Parses a command line argument of year or month.

    >>> parse_date_argument('2022')
    Year(year=2022)
    >>> parse_date_argument('may')
    Month(month=5)
    >>> parse_date_argument('2021-10')
    YearMonth(year=2021, month=10)
    """
    if re.match(r"^\d+$", s):
        return Year(int(s))
    elif re.match(r"^[a-z]+$", s):
        return Month(typing.cast(int, s))
    elif m := re.match(r"^(\d+)-(\d\d)$", s):
        year = int(m.group(1))
        month = month_to_abbrev(int(m.group(2)))
        return YearMonth(year, typing.cast(int, month))
    else:
        raise ValueError(f'unsupported type of argument: {s}')


def date_argument_to_date_range(s: str | None, *, default_year: int) -> DateRange:
    """
    Convert a date argument into a `DateRange` object.

    >>> period = date_argument_to_date_range(None, default_year = 2021)
    >>> period.begin
    datetime.date(2021, 1, 1)
    >>> period.end
    datetime.date(2022, 1, 1)

    >>> period = date_argument_to_date_range('1990', default_year = 2021)
    >>> period.begin
    datetime.date(1990, 1, 1)
    >>> period.end
    datetime.date(1991, 1, 1)

    >>> period = date_argument_to_date_range('mar', default_year = 2021)
    >>> period.begin
    datetime.date(2021, 3, 1)
    >>> period.end
    datetime.date(2021, 4, 1)

    >>> period = date_argument_to_date_range('2020-12', default_year = 2021)
    >>> period.begin
    datetime.date(2020, 12, 1)
    >>> period.end
    datetime.date(2021, 1, 1)
    """
    if s:
        match parse_date_argument(s):
            case Year(year):
                return DateRange(year)
            case Month(month):
                return DateRange(default_year, month)
            case YearMonth(year, month):
                return DateRange(year, month)
            case _:
                raise ValueError('unsupported input')
    else:
        return DateRange(default_year)
