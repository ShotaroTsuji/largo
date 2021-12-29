from largo.bs_command import BsCommand
from largo.pl_command import PlCommand
from cleo import Application

application = Application()
application.add(BsCommand())
application.add(PlCommand())


def main():
    application.run()
