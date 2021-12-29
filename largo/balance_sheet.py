import subprocess
from largo.project import Project
from largo.ledger_invoke import LedgerInvoke


class BalanceSheet(LedgerInvoke):
    def __init__(self, project: Project):
        self.project = project

    @property
    def command_arguments(self) -> list[str]:
        arguments = [self.project.ledger_bin, '-f', '-', 'balance',
                     self.project.account.assets,
                     self.project.account.liabilities,
                     self.project.account.equity]

        settings = self.project.bs_command
        if settings:
            arguments.extend(settings.default_options)

        return arguments
