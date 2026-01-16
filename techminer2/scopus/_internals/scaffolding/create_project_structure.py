from pathlib import Path

_DIRECTORIES = [
    "data/processed",
    "data/my_keywords",
    "data/thesaurus",
    "outputs",
    "outputs/tables",
    "outputs/figures",
    "outputs/texts",
    "outputs/section_1_introduction",
    "outputs/section_2_literature_review",
    "outputs/section_3_methodology",
    "outputs/section_4_results",
    "outputs/section_5_discussion",
    "outputs/section_6_synthesis",
    "outputs/section_7_conclusions",
    "outputs/section_8_references",
    "src",
]


_FILES = [
    "data/processed/_do_not_touch_.txt",
    "data/my_keywords/stopwords.txt",
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
