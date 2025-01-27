# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
"""Functions to sort the axes of a DataFrame."""
import pandas as pd  # type: ignore


class SortAxesMixin:

    def sort_columns(self, data_frame):

        # extracts the field terms
        counters = pd.DataFrame({"term": data_frame.columns.tolist()})

        # extracts the term occurreces
        counters["OCC"] = counters.term.str.split()
        counters["OCC"] = counters["OCC"].map(lambda x: x[-1])
        counters["OCC"] = counters["OCC"].str.split(":")
        counters["OCC"] = counters["OCC"].map(lambda x: x[0]).astype(int)

        # extracts the term citations
        counters["citations"] = counters.term.str.split()
        counters["citations"] = counters["citations"].map(lambda x: x[-1])
        counters["citations"] = counters["citations"].str.split(":")
        counters["citations"] = counters["citations"].map(lambda x: x[1]).astype(int)

        # sort the terms by the number of occurrences and citations
        counters = counters.sort_values(
            by=["OCC", "citations", "term"], ascending=[False, False, True]
        )
        sorted_topics = counters.term.tolist()

        # sort the columns of the DataFrame
        data_frame = data_frame[sorted_topics]

        return data_frame
