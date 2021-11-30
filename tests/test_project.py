import pytest
from largo.project import Project, StructureError, MissingBookError


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

    project = Project(shared_datadir / 'empty-manifest' / 'Largo.toml')
    with pytest.raises(KeyError):
        project.account.assets


def test_look_up_2021_book(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    want = shared_datadir / 'simple-project' / 'book' / '2021.ledger'
    assert project.book(2021) == want


def test_look_up_missing_book(shared_datadir):
    project = Project(shared_datadir / 'simple-project' / 'Largo.toml')
    with pytest.raises(MissingBookError):
        project.book(1900)
