from cleo.commands.command import Command
from cleo.helpers import argument, option
from largo.project import Project
from largo.balance_sheet import BalanceSheet
from largo.date_range import date_argument_to_date_range


class BsCommand(Command):
    name = "bs"
    description = "Show balance sheet"
    arguments = [
        argument(
            name="date-argument",
            description="The year/month of the balance sheet",
            optional=True,
        ),
    ]
    options = [
        option(
            long_name="manifest-path",
            description="The path to a manifest file",
            flag=False,
            default="Largo.toml"
        )
    ]

    def handle(self):
        project = Project(manifest_path=self.option('manifest-path'))

        date_argument = self.argument('date-argument')

        date_range = date_argument_to_date_range(date_argument, default_year=project.latest_year())

        bs = BalanceSheet(project, date_range)
        bs.build()