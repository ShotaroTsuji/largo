import pytest


@pytest.fixture
def simple_project(shared_datadir):
    return shared_datadir / 'simple-project' / 'Largo.toml'


@pytest.fixture
def japanese_manifest(shared_datadir):
    return shared_datadir / 'japanese-manifest' / 'Largo.toml'


@pytest.fixture
def empty_manifest(shared_datadir):
    return shared_datadir / 'empty-manifest' / 'Largo.toml'
