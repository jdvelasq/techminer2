from .s04_ctry_scopus import _create_ctry_col, _create_ctry_thesaurus


def s04_ctry_wos(root_directory: str) -> int:

    _create_ctry_col(root_directory=root_directory)
    _create_ctry_thesaurus(root_directory=root_directory)

    return 1
