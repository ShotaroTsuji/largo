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


class MissingBookError(Error):
    """Exception raised when the specified book is missing.

    Attributes:
        path -- missing book
    """

    def __init__(self, path):
        self.path = path


class Account:
    """Wrapper for account names dictionary"""

    def __init__(self, account):
        self.account = account

    @property
    def assets(self):
        return self.account['assets']

    @property
    def liabilities(self):
        return self.account['liabilities']

    @property
    def equity(self):
        return self.account['equity']


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

    @property
    def ledger_bin(self):
        return 'ledger'

    @property
    def account(self):
        return Account(self.manifest['account'])

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

    def book(self, year):
        """Returns the ledger book of the specified year"""
        book_path = self.project_root / 'book' / f'{year}.ledger'

        if not book_path.exists():
            raise MissingBookError(book_path)

        return book_path
