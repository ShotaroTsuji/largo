from cleo import Command


class BsCommand(Command):
    """
    Show balance sheet

    bs
        {--manifest-path=Largo.toml : The path to a manifest file}
    """

    def handle(self):
        print(self.option('manifest-path'))
