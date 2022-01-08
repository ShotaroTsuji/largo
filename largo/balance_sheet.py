import subprocess
from largo.project import Project
from largo.ledger_invoke import LedgerInvoke
from typing import List


class BalanceSheet(LedgerInvoke):
    def __init__(self, project: Project, year: int):
        self._project = project
        self._year = year

    @property
    def project(self) -> Project:
        return self._project

    @property
    def year(self) -> int:
        return self._year

    @property
    def command_arguments(self) -> List[str]:
        arguments = [self.project.ledger_bin, '-f', '-', 'balance',
                     self.project.account.assets,
                     self.project.account.liabilities,
                     self.project.account.equity]

        settings = self.project.bs_command
        if settings:
            arguments.extend(settings.default_options)

        return arguments
