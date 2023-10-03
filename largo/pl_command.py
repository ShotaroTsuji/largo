from cleo.commands.command import Command
from cleo.helpers import argument, option
from largo.date_range import date_argument_to_date_range
from largo.project import Project
from largo.profit_loss import ProfitLoss
from typing import cast


class PlCommand(Command):
    """
    Show Profit/Loss

    pl
        {--manifest-path=Largo.toml : The path to a manifest file}
        {date-argument? : Year/month to be shown}
    """
    name="pl"
    arguments=[
        argument(
            name="date-argument",
            description="Year/month to be shown",
            optional=True,
        )
    ]
    options=[
        option(
            long_name="manifest-path",
            description="The path to a manifest file",
            flag=False,
            default="Largo.toml",
        )
    ]


    def handle(self):
        project = Project(manifest_path=cast(str, self.option('manifest-path')))

        date_argument = self.argument('date-argument')

        date_range = date_argument_to_date_range(date_argument, default_year=project.latest_year())

        pl = ProfitLoss(project, date_range=date_range)
        pl.build()
