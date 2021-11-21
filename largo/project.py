import toml
from pathlib import Path


class Error(Exception):
    """Base class for exceptions in the project module."""
    pass


class StructureError(Error):
    """Exception raised for errors in structure checking.

    Attributes:
        missing -- missing elements
    """

    def __init__(self, missing):
        self.missing = missing


class Project:
    """
    Represents a ledger project
    """

    def __init__(self, manifest_path):
        self.manifest_path = Path(manifest_path)
        self.project_root = self.manifest_path.parent

        self.check_structure()

        self.manifest = toml.load(self.manifest_path)

    def __str__(self):
        return f'Project {{ manifest_path: {self.manifest_path} }}'

    def check_structure(self):
        """
        Check the structure of project files
        """
        missing = []
        book_dir = self.project_root / 'book'

        if not self.manifest_path.exists():
            missing.append(self.manifest_path)

        if not book_dir.exists():
            missing.append(book_dir)

        if missing:
            raise StructureError(missing)
        else:
            return True
