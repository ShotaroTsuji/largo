from abc import ABCMeta, abstractmethod
from typing import List
from largo.project import Project
import subprocess


class LedgerInvoke(metaclass=ABCMeta):
    @property
    @abstractmethod
    def command_arguments(self) -> List[str]:
        pass

    @property
    @abstractmethod
    def project(self) -> Project:
        pass

    @property
    @abstractmethod
    def year(self) -> int:
        pass

    def read_book(self) -> bytes:
        book_path = self.project.book(self.year)

        with open(book_path, mode='rb') as book_file:
            book = book_file.read()

        return book

    def build(self) -> subprocess.CompletedProcess:
        book = self.read_book()
        return subprocess.run(args=self.command_arguments, input=book)
