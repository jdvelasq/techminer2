import pathlib


def internal__get_user_thesaurus_file_path(params):
    """:meta private:"""

    return (
        pathlib.Path(params.root_directory) / "data/thesaurus" / params.thesaurus_file
    )
