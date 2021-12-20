from cleo import Command
from largo.project import Project
from largo.balance_sheet import BalanceSheet
import datetime


def current_year():
    return datetime.date.today().year


class BsCommand(Command):
    """
    Show balance sheet

    bs
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))
        bs = BalanceSheet(project)
        bs.build(current_year())
