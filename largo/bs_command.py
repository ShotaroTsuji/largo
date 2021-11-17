from cleo import Command
from largo.project import Project


class BsCommand(Command):
    """
    Show balance sheet

    bs
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))
        print(project)
