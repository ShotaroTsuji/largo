from largo.bs_command import BsCommand
from largo.pl_command import PlCommand
from largo.cf_command import CfCommand
from cleo.application import Application

application = Application()
application.add(BsCommand())
application.add(PlCommand())
application.add(CfCommand())


def main():
    application.run()
