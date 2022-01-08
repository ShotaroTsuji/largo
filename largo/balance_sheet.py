from largo.project import Project
from largo.ledger_invoke import LedgerInvoke
from largo.date_range import DateRange
from typing import List
import datetime


class BalanceSheet(LedgerInvoke):
    def __init__(self, project: Project, date_range: DateRange):
        self._project = project
        self._date_range = date_range

    @property
    def project(self) -> Project:
        return self._project

    @property
    def accounts(self) -> List[str]:
        return [self.project.account.assets,
                self.project.account.liabilities,
                self.project.account.equity]

    @property
    def year(self) -> int:
        return self._date_range.year

    @property
    def ledger_subcommand(self) -> str:
        return 'balance'

    @property
    def period_begin(self) -> datetime.date:
        return self._date_range.begin

    @property
    def period_end(self) -> datetime.date:
        return self._date_range.end

    @property
    def default_options(self) -> List[str]:
        if settings := self.project.bs_command:
            return settings.default_options
        else:
            return []
