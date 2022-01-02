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
        {date-argument? : Year/month to be shown}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))

        date_argument = self.argument('date-argument')

        if date_argument:
            arg_type, arg = parse_argument(date_argument)
            if arg_type is ArgumentType.YEAR:
                year = arg
                month = None
            elif arg_type is ArgumentType.MONTH:
                year = project.latest_year()
                month = arg
        else:
            year = project.latest_year()
            month = None

        date_range = DateRange(year, month)

        pl = ProfitLoss(project, date_range=date_range)
        pl.build(year)
