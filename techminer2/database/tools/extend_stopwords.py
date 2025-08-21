# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=attribute-defined-outside-init

"""
Extend Stopwords
===============================================================================


Example:
    >>> from techminer2.database.tools import ExtendStopwords
    >>> (
    ...     ExtendStopwords()
    ...     .with_patterns(["finance", "investment"])
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )

    >>> from pprint import pprint
    >>> with open("examples/fintech/data/my_keywords/stopwords.txt", "r", encoding="utf-8") as file:
    ...     stopwords = [line.strip() for line in file.readlines()]
    ...     pprint(stopwords)
    ['finance', 'investment']



"""

import pathlib

from techminer2._internals.mixins import ParamsMixin


class ExtendStopwords(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__set_filepath(self):
        self.file_path = (
            pathlib.Path(self.params.root_directory) / "data/my_keywords/stopwords.txt"
        )

    # -------------------------------------------------------------------------
    def internal__load_stopwords(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.stopwords = [line.strip() for line in file.readlines()]

    # -------------------------------------------------------------------------
    def internal__extend_stopwords(self):
        self.stopwords.extend(self.params.pattern)
        self.stopwords = sorted(set(self.stopwords))

    # -------------------------------------------------------------------------
    def internal__save_stopwords(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for word in self.stopwords:
                file.write(f"{word}\n")

    # -------------------------------------------------------------------------
    def run(self):
        """Runs the command."""

        self.internal__set_filepath()
        self.internal__load_stopwords()
        self.internal__extend_stopwords()
        self.internal__save_stopwords()
