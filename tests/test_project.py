import pytest
from largo.project import Project, StructureError, MissingBookError


def test_structure_check(simple_project):
    Project(simple_project)


def test_structure_check_of_empty_dir(tmpdir):
    with pytest.raises(StructureError):
        Project(tmpdir / 'Largo.toml')


def test_account_names(simple_project, japanese_manifest, empty_manifest):
    project = Project(simple_project)
    assert project.account.assets == 'Assets'
    assert project.account.liabilities == 'Liabilities'
    assert project.account.equity == 'Equity'
    assert project.account.expenses == 'Expenses'
    assert project.account.income == 'Income'
    assert project.account.cash == ['Assets:Cash']

    project = Project(japanese_manifest)
    assert project.account.assets == '資産'
    assert project.account.liabilities == '負債'
    assert project.account.equity == '純資産'
    assert project.account.expenses == '費用'
    assert project.account.income == '収益'
    assert project.account.cash == ['資産:現金', '資産:普通預金']

    project = Project(empty_manifest)
    with pytest.raises(KeyError):
        project.account.assets


def test_look_up_2021_book(shared_datadir, simple_project):
    project = Project(simple_project)
    want = shared_datadir / 'simple-project' / 'book' / '2021.ledger'
    assert project.book(2021) == want


def test_look_up_missing_book(simple_project):
    project = Project(simple_project)
    with pytest.raises(MissingBookError):
        project.book(1900)


def test_get_the_latest_year_of_books(simple_project, non_numeric_books):
    project = Project(simple_project)
    assert project.latest_year() == 2021

    project = Project(non_numeric_books)
    with pytest.raises(Exception):
        project.latest_year()
