from pathlib import Path

_DIRECTORIES = [
    "analyze",
    "ingest/processed",
    "refine/thesaurus",
    "refine/word_lists",
    "report",
    "report/manuscript/section_1_introduction",
    "report/manuscript/section_2_literature_review",
    "report/manuscript/section_3_methodology",
    "report/manuscript/section_4_results",
    "report/manuscript/section_5_discussion",
    "report/manuscript/section_6_synthesis",
    "report/manuscript/section_7_conclusions",
    "report/manuscript/section_8_references",
    "report/manusctipt",
    "report/visualize",
    "src",
]


_FILES = [
    "ingest/processed/_do_not_touch_.txt",
    "refine/word_lists/countries.ignore.txt",
    "refine/word_lists/organizations.ignore.txt",
    "refine/word_lists/full_keywords.ignore.txt",
]


# ----------------------------------------------------------------------------
def _create_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------------
def _create_file(path: Path) -> None:
    if not path.exists():
        path.touch()


# ----------------------------------------------------------------------------
def create_project_structure(root_directory: str) -> None:

    root = Path(root_directory)

    for directory in _DIRECTORIES:
        _create_directory(root / directory)

    for file in _FILES:
        _create_file(root / file)


# ----------------------------------------------------------------------------
