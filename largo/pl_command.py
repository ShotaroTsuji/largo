from cleo import Command
from largo.date_range import DateRange
from largo.project import Project
from largo.profit_loss import ProfitLoss


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
