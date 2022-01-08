from largo.date_range import DateRange
from largo.project import Project
from largo.ledger_invoke import LedgerInvoke
from typing import List
import subprocess


class ProfitLoss(LedgerInvoke):
    def __init__(self, project: Project, date_range: DateRange):
        self._project = project
        self._date_range = date_range

    @property
    def project(self) -> Project:
        return self._project

    @property
    def accounts(self) -> list[str]:
        return [self.project.account.expenses, self.project.account.income]

    @property
    def year(self) -> int:
        return self._date_range.year

    @property
    def command_arguments(self) -> List[str]:
        arguments = [self.project.ledger_bin, '-f', '-', 'balance']

        if self._date_range:
            arguments.extend(['-b', str(self._date_range.begin), '-e', str(self._date_range.end)])

        arguments.extend(self.accounts)

        settings = self.project.pl_command
        if settings:
            arguments.extend(settings.default_options)

        return arguments
