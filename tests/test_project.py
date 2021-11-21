import pytest
from largo.project import Project, StructureError


def test_structure_check(shared_datadir):
    Project(shared_datadir / 'simple-project' / 'Largo.toml')


def test_structure_check_of_empty_dir(tmpdir):
    with pytest.raises(StructureError):
        Project(tmpdir / 'Largo.toml')


def test_account_names(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    assert project.account.assets == 'Assets'
    assert project.account.liabilities == 'Liabilities'
    assert project.account.equity == 'Equity'

    project = Project(shared_datadir / 'japanese-manifest' / 'Largo.toml')
    assert project.account.assets == '資産'
    assert project.account.liabilities == '負債'
    assert project.account.equity == '純資産'
