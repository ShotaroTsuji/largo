from largo.balance_sheet import BalanceSheet
from largo.project import Project


def test_init_balance_sheet(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    BalanceSheet(project)


def test_bs_command_arguments(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    bs = BalanceSheet(project)
    want = bs.command_arguments
    assert want == ['ledger', '-f', '-',
                    'balance', 'Assets', 'Liabilities', 'Equity']

    project = Project(shared_datadir / 'japanese-manifest' / 'Largo.toml')
    bs = BalanceSheet(project)
    want = bs.command_arguments
    assert want == ['ledger', '-f', '-', 'balance', '資産', '負債', '純資産']


def test_build_balance_sheet(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    bs = BalanceSheet(project)
    assert 0 == bs.build(2021)

    project = Project(shared_datadir / 'japanese-manifest' / 'Largo.toml')
    bs = BalanceSheet(project)
    assert 0 == bs.build(2021)
