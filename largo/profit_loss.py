from largo.project import Project
from largo.ledger_invoke import LedgerInvoke
from typing import List
import subprocess


class ProfitLoss(LedgerInvoke):
    def __init__(self, project: Project, month = None):
        self._project = project
        self._month = month

    @property
    def project(self) -> Project:
        return self._project

    @property
    def accounts(self) -> list[str]:
        return [self.project.account.expenses, self.project.account.income]

    @property
    def command_arguments(self) -> List[str]:
        arguments = [self.project.ledger_bin, '-f', '-', 'balance']

        if self._month:
            begin, end = self._month.to_range_str()
            arguments.extend(['-b', begin])
            if end:
                arguments.extend(['-e', end])

        arguments.extend(self.accounts)

        settings = self.project.pl_command
        if settings:
            arguments.extend(settings.default_options)

        return arguments
