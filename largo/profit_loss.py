from largo.project import Project
from largo.ledger_invoke import LedgerInvoke
from typing import List
import subprocess


class ProfitLoss(LedgerInvoke):
    def __init__(self, project: Project):
        self._project = project

    @property
    def project(self) -> Project:
        return self._project

    @property
    def command_arguments(self) -> List[str]:
        arguments = [self.project.ledger_bin, '-f', '-', 'balance',
                     self.project.account.expenses,
                     self.project.account.income]

        settings = self.project.pl_command
        if settings:
            arguments.extend(settings.default_options)

        return arguments
