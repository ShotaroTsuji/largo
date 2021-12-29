from largo.project import Project
from largo.ledger_invoke import LedgerInvoke
import subprocess


class ProfitLoss(LedgerInvoke):
    def __init__(self, project: Project):
        self.project = project

    @property
    def command_arguments(self) -> list[str]:
        arguments = [self.project.ledger_bin, '-f', '-', 'balance',
                     self.project.account.expenses,
                     self.project.account.income]

        return arguments
