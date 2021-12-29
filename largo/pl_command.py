from cleo import Command
from largo.project import Project


class PlCommand(Command):
    """
    Show Profit/Loss

    pl
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))
