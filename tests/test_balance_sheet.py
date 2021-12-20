from largo.balance_sheet import BalanceSheet
from largo.project import Project


def test_init_balance_sheet(simple_project):
    project = Project(simple_project)
    BalanceSheet(project)


def test_bs_command_arguments(simple_project, japanese_manifest):
    project = Project(simple_project)
    bs = BalanceSheet(project)
    want = bs.command_arguments
    assert want == ['ledger', '-f', '-',
                    'balance', 'Assets', 'Liabilities', 'Equity']

    project = Project(japanese_manifest)
    bs = BalanceSheet(project)
    want = bs.command_arguments
    assert want == ['ledger', '-f', '-', 'balance', '資産', '負債', '純資産']


def test_build_balance_sheet(simple_project, japanese_manifest):
    project = Project(simple_project)
    bs = BalanceSheet(project)
    assert 0 == bs.build(2021)

    project = Project(japanese_manifest)
    bs = BalanceSheet(project)
    assert 0 == bs.build(2021)
