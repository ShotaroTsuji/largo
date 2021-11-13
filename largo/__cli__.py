from largo.bs_command import BsCommand
from cleo import Application

application = Application()
application.add(BsCommand())


def main():
    application.run()
