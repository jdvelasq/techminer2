# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Search for abbreviations in a thesaurus."""
import sys


def internal__preprocess_abbreviations(root_dir):

    from .....thesaurus.abbreviations import CreateThesaurus

    sys.stderr.write("INFO  Preprocessing abbreviations\n")
    sys.stderr.flush()

    CreateThesaurus(root_directory=root_dir).run()
