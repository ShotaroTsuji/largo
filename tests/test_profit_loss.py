from largo.profit_loss import ProfitLoss
from largo.project import Project
from largo.pl_command import Month


def test_pl_command_arguments(simple_project, japanese_manifest):
    project = Project(simple_project)
    pl = ProfitLoss(project)
    want = [project.ledger_bin, '-f', '-', 'balance', 'Expenses', 'Income']
    assert want == pl.command_arguments

    pl = ProfitLoss(project, month=Month('jan'))
    want = [project.ledger_bin, '-f', '-', 'balance', '-b', 'jan', '-e', 'feb', 'Expenses', 'Income']
    assert want == pl.command_arguments

    pl = ProfitLoss(project, month=Month('dec'))
    want = [project.ledger_bin, '-f', '-', 'balance', '-b', 'dec', 'Expenses', 'Income']
    assert want == pl.command_arguments

    project = Project(japanese_manifest)
    pl = ProfitLoss(project)
    want = [project.ledger_bin, '-f', '-', 'balance', '費用', '収益', '--no-pager']
    assert want == pl.command_arguments


def test_build_profit_loss(simple_project, japanese_manifest):
    project = Project(simple_project)
    bs = ProfitLoss(project)
    assert 0 == bs.build(2021).returncode

    project = Project(japanese_manifest)
    bs = ProfitLoss(project)
    assert 0 == bs.build(2021).returncode
