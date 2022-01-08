from largo.date_range import DateRange
from largo.project import Project
from largo.cash_flow import CashFlow


def test_cf_command_arguments(japanese_manifest):
    project = Project(japanese_manifest)
    cf = CashFlow(project, DateRange(2021))

    want = [project.ledger_bin, '-f', '-',
            'balance', '-b', '2021-01-01', '-e', '2022-01-01',
            '資産:現金', '資産:普通預金']
    assert want == cf.command_arguments

def test_build_cash_flow(japanese_manifest):
    project = Project(japanese_manifest)
    cf = CashFlow(project, DateRange(2021, 5))
    assert 0 == cf.build().returncode
