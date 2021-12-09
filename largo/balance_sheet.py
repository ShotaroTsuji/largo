from largo.project import Project


class BalanceSheet:
    def __init__(self, project: Project):
        self.project = project

    @property
    def command_arguments(self):
        return [self.project.ledger_bin, '-f', '-', 'balance',
                self.project.account.assets,
                self.project.account.liabilities,
                self.project.account.equity]
