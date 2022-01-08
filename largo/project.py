import toml
from largo import PathLike
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Iterator


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
    expenses: str
    income: str
    cash: List[str]


@dataclass
class Bs:
    """Settings for bs subcommand"""
    default_options: list[str] = field(default_factory=list)


@dataclass
class Pl:
    """Settings for pl subcommand"""
    default_options: list[str] = field(default_factory=list)


@dataclass
class Cf:
    """Settings for cf subcommand"""
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
    def book_dir(self) -> Path:
        return self.project_root / 'book'

    @property
    def ledger_bin(self) -> str:
        return 'ledger'

    @property
    def account(self) -> Account:
        try:
            return Account(**self.manifest['account'])
        except TypeError as exc:
            raise ValueError('Some fields in `[account]` of Largo.toml are missing') from exc

    @property
    def command(self) -> Optional[dict]:
        return self.manifest.get('command')

    @property
    def bs_command(self) -> Optional[Bs]:
        if command := self.command:
            if bs := command.get('bs'):
                return Bs(**bs)
        return None

    @property
    def pl_command(self) -> Optional[Pl]:
        if command := self.command:
            if pl := command.get('pl'):
                return Pl(**pl)
        return None

    @property
    def cf_command(self) -> Optional[Cf]:
        if command := self.command:
            if cf := command.get('cf'):
                return Cf(**cf)
        return None

    def check_structure(self) -> bool:
        """
        Check the structure of project files
        """
        missing = []

        if not self.manifest_path.exists():
            missing.append(self.manifest_path)

        if not self.book_dir.exists():
            missing.append(self.book_dir)

        if missing:
            raise StructureError(missing)
        else:
            return True

    def book(self, year: int) -> Path:
        """Returns the ledger book of the specified year"""
        book_path = self.book_dir / f'{year}.ledger'

        if not book_path.exists():
            raise MissingBookError(book_path)

        return book_path

    def latest_year(self) -> int:
        """Returns the latest year of the books"""
        latest = max(self.list_books(), key=lambda p: p.stem)
        return int(latest.stem)

    def list_books(self) -> Iterator[Path]:
        """Returns the ledger books"""
        return self.book_dir.glob('*.ledger')
