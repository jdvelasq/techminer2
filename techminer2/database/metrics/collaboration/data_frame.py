# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Data Frame
===============================================================================

>>> from techminer2.database.metrics.collaboration import DataFrame
>>> (
...     DataFrame()
...     #
...     # FIELD:
...     .with_field("countries")
...     .having_terms_in_top(20)
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head()
               OCC  global_citations  ...  multiple_publication  mp_ratio
countries                             ...                                
United States   16              3189  ...                     8      0.50
China            8              1085  ...                     5      0.62
Germany          7              1814  ...                     3      0.43
South Korea      6              1192  ...                     2      0.33
Australia        5               783  ...                     4      0.80
<BLANKLINE>
[5 rows x 6 columns]
    
"""
from ...._internals.mixins import ParamsMixin
from ..._internals.io import internal__load_filtered_database
from ..performance.data_frame import DataFrame as PerformanceMetricsDataFrame


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_load_the_database(self):
        return internal__load_filtered_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_2_compute_collaboration_metrics(self, data_frame):

        field = self.params.field

        #
        # Add a column to represent the number of occurrences of a document
        data_frame = data_frame.copy()
        data_frame = data_frame.dropna(subset=[field])
        data_frame = data_frame.assign(OCC=1)

        #
        # Add columns to represent single and multiple publications for a document
        data_frame["single_publication"] = data_frame[field].map(
            lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0
        )
        data_frame["multiple_publication"] = data_frame[field].map(
            lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0
        )

        #
        # Split multi-topic documents into individual documents with one topic each
        exploded = data_frame[
            [
                field,
                "OCC",
                "global_citations",
                "local_citations",
                "single_publication",
                "multiple_publication",
                "record_id",
            ]
        ].copy()
        exploded[field] = exploded[field].str.split(";")
        exploded = exploded.explode(field)
        exploded[field] = exploded[field].str.strip()

        #
        # Compute collaboration indicators for each topic
        metrics = exploded.groupby(field, as_index=False).agg(
            {
                "OCC": "sum",
                "global_citations": "sum",
                "local_citations": "sum",
                "single_publication": "sum",
                "multiple_publication": "sum",
            }
        )

        #
        # Compute the multiple publication ratio for each topic
        metrics["mp_ratio"] = metrics["multiple_publication"] / metrics["OCC"]
        metrics["mp_ratio"] = metrics["mp_ratio"].round(2)

        #
        # Sort the topics by number of occurrences, global citations, and local
        # citations
        metrics = metrics.sort_values(
            by=["OCC", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

        #
        # Set the index to the criterion column
        metrics = metrics.set_index(field)

        return metrics

    # -------------------------------------------------------------------------
    def _step_3_filter_terms(self, data_frame):
        terms_in = PerformanceMetricsDataFrame()
        terms_in = terms_in.update(**self.params.__dict__)
        terms_in = terms_in.run()
        terms_in = terms_in.index
        data_frame = data_frame[data_frame.index.isin(terms_in)]
        return data_frame

    # -------------------------------------------------------------------------
    def run(self):
        database = self._step_1_load_the_database()
        data_frame = self._step_2_compute_collaboration_metrics(database)
        data_frame = self._step_3_filter_terms(data_frame)
        return data_frame
