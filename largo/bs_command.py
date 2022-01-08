from cleo import Command
from largo.project import Project
from largo.balance_sheet import BalanceSheet
import datetime


class BsCommand(Command):
    """
    Show balance sheet

    bs
        {year? : The year of the balance sheet}
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))

        year = self.argument('year')
        if year:
            year = int(year)
        else:
            year = project.latest_year()

        bs = BalanceSheet(project, year)
        bs.build()
