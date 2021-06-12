from pathlib import Path


def make_directory(path):
    Path(path).mkdir(parents = True, exist_ok = True)
