from cleo import Command
from largo.project import Project
from largo.balance_sheet import BalanceSheet
import datetime


def current_year() -> int:
    return datetime.date.today().year


class BsCommand(Command):
    """
    Show balance sheet

    bs
        {year? : The year of the balance sheet}
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))
        bs = BalanceSheet(project)
        year = self.argument('year')
        if year:
            bs.build(int(year))
        else:
            bs.build(current_year())
