# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import pathlib


def internal__generate_user_thesaurus_file_path(params):
    """:meta private:"""

    return pathlib.Path(params.root_dir) / "thesaurus" / params.thesaurus_file
