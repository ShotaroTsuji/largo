import pytest
from largo.project import Project, StructureError


def test_structure_check(shared_datadir):
    Project(shared_datadir / 'simple-project' / 'Largo.toml')


def test_structure_check_of_empty_dir(tmpdir):
    with pytest.raises(StructureError):
        Project(tmpdir / 'Largo.toml')
