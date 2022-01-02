import datetime

def month_abbrevs() -> list[str]:
    return ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
            'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def month_to_abbrev(i: int) -> str:
    return month_abbrevs()[i - 1]

def month_from_abbrev(s: str) -> int:
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
