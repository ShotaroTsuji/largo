from cleo import Command
from largo.date_range import DateRange
from largo.project import Project
from largo.profit_loss import ProfitLoss
from typing import Any, Tuple
import enum
import re


class ArgumentType(enum.Enum):
    YEAR = enum.auto()
    MONTH = enum.auto()


def parse_argument(s: str) -> Tuple[ArgumentType, Any]:
    if re.match(r"\d+", s):
        return (ArgumentType.YEAR, int(s))
    if re.match(r"[a-z]+", s):
        return (ArgumentType.MONTH, s)
    raise Exception(f'unsupported type of argument {s}')


class PlCommand(Command):
    """
    Show Profit/Loss

    pl
        {--manifest-path=Largo.toml : The path to a manifest file}
        {month? : Month to be shown}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))
        year = project.latest_year()
        date_range = DateRange(year, self.argument('month'))

        pl = ProfitLoss(project, date_range=date_range)
        pl.build(year)
