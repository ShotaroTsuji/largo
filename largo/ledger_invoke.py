from abc import ABCMeta, abstractmethod
from typing import List
from largo.project import Project
import subprocess
import datetime


class LedgerInvoke(metaclass=ABCMeta):
    @property
    @abstractmethod
    def project(self) -> Project:
        pass

    @property
    @abstractmethod
    def year(self) -> int:
        pass

    @property
    @abstractmethod
    def ledger_subcommand(self) -> str:
        pass

    @property
    @abstractmethod
    def accounts(self) -> List[str]:
        pass

    @property
    @abstractmethod
    def period_begin(self) -> datetime.date:
        pass

    @property
    @abstractmethod
    def period_end(self) -> datetime.date:
        pass

    @property
    @abstractmethod
    def default_options(self) -> List[str]:
        pass

    @property
    def period_arguments(self) -> List[str]:
        return ['-b', str(self.period_begin), '-e', str(self.period_end)]

    @property
    def command_arguments(self) -> List[str]:
        arguments = [self.project.ledger_bin, '-f', '-']

        arguments += [self.ledger_subcommand]
        arguments += self.period_arguments
        arguments += self.accounts
        arguments += self.default_options

        return arguments

    def read_book(self) -> bytes:
        book_path = self.project.book(self.year)

        with open(book_path, mode='rb') as book_file:
            book = book_file.read()

        return book

    def build(self) -> subprocess.CompletedProcess:
        book = self.read_book()
        return subprocess.run(args=self.command_arguments, input=book)


