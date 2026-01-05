# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Search String
=======================================================================================


Example:
    >>> from techminer2.database.tools import SearchString

    >>> (
    ...     SearchString()
    ...     #
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )




"""
import os.path

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io.load_filtered_records_from_database import (
    internal__load_filtered_records_from_database,
)


class SearchString(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        records = internal__load_filtered_records_from_database(params=self.params)
        titles = records.raw_document_title.to_list()

        # divide titles into chunks of 10
        chunks = [titles[i : i + 10] for i in range(0, len(titles), 10)]

        filepath = os.path.join(
            self.params.root_directory, "outputs/scopus_search_string.txt"
        )

        with open(filepath, "w") as f:
            f.write("(\n")
            for chunk in chunks:
                for index, title in enumerate(chunk):
                    if index == 0:
                        f.write(f"    TITLE{{{title}}}")
                    else:
                        f.write(f"\n    OR TITLE{{{title}}}")

                    if index == len(chunk) - 1:
                        if chunk != chunks[-1]:
                            f.write("\n) OR (\n")
                        else:
                            f.write("\n)\n")
