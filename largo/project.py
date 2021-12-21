import toml
from largo import PathLike
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


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

    def __init__(self, path: PathLike):
        self.path = path


@dataclass
class Account:
    """Wrapper for account names dictionary"""
    assets: str
    liabilities: str
    equity: str


@dataclass
class Bs:
    """Settings for bs subcommand"""
    default_options: list[str] = field(default_factory=list)


class Project:
    """
    Represents a ledger project
    """

    def __init__(self, manifest_path: PathLike):
        self.manifest_path = Path(manifest_path)
        self.project_root = self.manifest_path.parent

        self.check_structure()

        self.manifest = toml.load(self.manifest_path)

    def __str__(self) -> str:
        return f'Project {{ manifest_path: {self.manifest_path} }}'

    @property
    def ledger_bin(self) -> str:
        return 'ledger'

    @property
    def account(self) -> Account:
        return Account(**self.manifest['account'])

    @property
    def bs_command(self) -> Optional[Bs]:
        if not self.manifest.get('command'):
            return None

        if not self.manifest['command'].get('bs'):
            return None

        return Bs(**self.manifest['command']['bs'])

    def check_structure(self) -> bool:
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

    def book(self, year: int) -> Path:
        """Returns the ledger book of the specified year"""
        book_path = self.project_root / 'book' / f'{year}.ledger'

        if not book_path.exists():
            raise MissingBookError(book_path)

        return book_path
