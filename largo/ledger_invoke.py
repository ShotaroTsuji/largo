from abc import ABCMeta, abstractmethod
from typing import List
from largo.project import Project
import subprocess


class LedgerInvoke(metaclass=ABCMeta):
    @abstractmethod
    def command_arguments(self) -> List[str]:
        pass

    @property
    @abstractmethod
    def project(self) -> Project:
        pass

    def read_book(self, year: int) -> bytes:
        book_path = self.project.book(year)

        with open(book_path, mode='rb') as book_file:
            book = book_file.read()

        return book

    def build(self, year: int) -> subprocess.CompletedProcess:
        book = self.read_book(year)
        return subprocess.run(args=self.command_arguments, input=book)
