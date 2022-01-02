from cleo import Command
from largo.project import Project
from largo.profit_loss import ProfitLoss
from typing import Optional, Tuple


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


class PlCommand(Command):
    """
    Show Profit/Loss

    pl
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))
        pl = ProfitLoss(project)
        pl.build(project.latest_year())
