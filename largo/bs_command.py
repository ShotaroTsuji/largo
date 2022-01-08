from cleo import Command
from largo.project import Project
from largo.balance_sheet import BalanceSheet
from largo.date_range import DateRange, date_argument_to_date_range


class BsCommand(Command):
    """
    Show balance sheet

    bs
        {date-argument? : The year/month of the balance sheet}
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))

        date_argument = self.argument('date-argument')

        date_range = date_argument_to_date_range(date_argument, default_year=project.latest_year())

        bs = BalanceSheet(project, date_range)
        bs.build()
