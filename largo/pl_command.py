from cleo import Command
from largo.project import Project
from largo.profit_loss import ProfitLoss


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
