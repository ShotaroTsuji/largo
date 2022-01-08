from largo.date_range import DateRange
from largo.profit_loss import ProfitLoss
from largo.project import Project


def test_pl_command_arguments(simple_project):
    project = Project(simple_project)

    pl = ProfitLoss(project, date_range=DateRange(2021, 'jan'))
    want = [project.ledger_bin, '-f', '-', 'balance',
            '-b', '2021-01-01', '-e', '2021-02-01', 'Expenses', 'Income']
    assert want == pl.command_arguments

    pl = ProfitLoss(project, date_range=DateRange(2021, 'dec'))
    want = [project.ledger_bin, '-f', '-', 'balance',
            '-b', '2021-12-01', '-e', '2022-01-01', 'Expenses', 'Income']
    assert want == pl.command_arguments


def test_build_profit_loss(simple_project, japanese_manifest):
    project = Project(simple_project)
    bs = ProfitLoss(project, DateRange(2021))
    assert 0 == bs.build().returncode

    project = Project(japanese_manifest)
    bs = ProfitLoss(project, DateRange(2021))
    assert 0 == bs.build().returncode
