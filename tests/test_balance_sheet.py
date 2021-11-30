from largo.balance_sheet import BalanceSheet
from largo.project import Project


def test_init_balance_sheet(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    BalanceSheet(project)
