from cleo import Command
from largo.date_range import month_to_abbrev, DateRange
from largo.project import Project
from largo.profit_loss import ProfitLoss
from typing import Any, Optional, Tuple, cast
import enum
import re


class ArgumentType(enum.Enum):
    YEAR = enum.auto()
    MONTH = enum.auto()
    YEAR_MONTH = enum.auto()


def parse_argument(s: str) -> Tuple[ArgumentType, Any]:
    if re.match(r"\d+$", s):
        return (ArgumentType.YEAR, int(s))
    if re.match(r"[a-z]+$", s):
        return (ArgumentType.MONTH, s)
    if m := re.match(r"(\d+)-(\d\d)$", s):
        year = int(m.group(1))
        month = month_to_abbrev(int(m.group(2)))
        return (ArgumentType.YEAR_MONTH, (year, month))
    else:
        raise Exception(f'unsupported type of argument {s}')


def date_argument_to_year_month(date_argument: str, *, default_year: int) -> Tuple[int, Optional[int]]:
        if date_argument:
            arg_type, arg = parse_argument(date_argument)
            if arg_type is ArgumentType.YEAR:
                return (arg, None)
            elif arg_type is ArgumentType.MONTH:
                return (default_year, arg)
            elif arg_type is ArgumentType.YEAR_MONTH:
                year, month = arg
                return (year, cast(int, month))
            else:
                raise ValueError('Unreachable!')
        else:
            return (default_year, None)


class PlCommand(Command):
    """
    Show Profit/Loss

    pl
        {--manifest-path=Largo.toml : The path to a manifest file}
        {date-argument? : Year/month to be shown}
    """

    def handle(self):
        project = Project(manifest_path=cast(str, self.option('manifest-path')))

        date_argument = cast(str, self.argument('date-argument'))

        year, month = date_argument_to_year_month(date_argument, default_year=project.latest_year())

        date_range = DateRange(year, month)

        pl = ProfitLoss(project, date_range=date_range)
        pl.build(year)
