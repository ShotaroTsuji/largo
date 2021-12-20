import subprocess
from largo.project import Project


class BalanceSheet:
    def __init__(self, project: Project):
        self.project = project

    @property
    def command_arguments(self) -> list[str]:
        return [self.project.ledger_bin, '-f', '-', 'balance',
                self.project.account.assets,
                self.project.account.liabilities,
                self.project.account.equity]

    def read_book(self, year: int) -> bytes:
        book_path = self.project.book(year)

        with open(book_path, mode='rb') as book_file:
            book = book_file.read()

        return book

    def build(self, year: int) -> subprocess.CompletedProcess:
        book = self.read_book(year)
        return subprocess.run(self.command_arguments, input=book)
