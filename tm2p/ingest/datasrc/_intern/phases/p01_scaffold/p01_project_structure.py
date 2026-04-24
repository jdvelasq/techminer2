from pathlib import Path

_DIRECTORIES = [
    "ingest/process",
    "refine/thesaurus",
    "refine/word_lists",
    "report/",
    "src",
]


_FILES = [
    "ingest/process/_do_not_touch_.txt",
]


# ----------------------------------------------------------------------------
def _create_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------------
def _create_file(path: Path) -> None:
    if not path.exists():
        path.touch()


# ----------------------------------------------------------------------------
def p01_project_structure(root_directory: str) -> None:

    root = Path(root_directory)

    for directory in _DIRECTORIES:
        _create_directory(root / directory)

    for file in _FILES:
        _create_file(root / file)


# ----------------------------------------------------------------------------
