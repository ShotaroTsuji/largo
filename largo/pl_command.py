from cleo import Command
from largo import Month
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
        pl = ProfitLoss(project, month=self.month)
        pl.build(project.latest_year())

    @property
    def month(self):
        month = self.argument('month')
        if month:
            return Month(month)
        else:
            return None
