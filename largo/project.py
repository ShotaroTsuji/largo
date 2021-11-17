from pathlib import Path


class Project:
    """
    Represents a ledger project
    """

    def __init__(self, manifest_path):
        self.manifest_path = Path(manifest_path)

    def __str__(self):
        return f'Project {{ manifest_path: {self.manifest_path} }}'
