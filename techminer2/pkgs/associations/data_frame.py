# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Term Associations Frame
===============================================================================


## >>> from techminer2.analyze.associations import DataFrame
## >>> associations = (
## ...     DataFrame()
## ...     .set_analysis_params(
## ...         item='FINTECH',
## ...     #
## ...     #
## ...     # COLUMNS:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(2, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # ROWS:
## ...     .with_other_field("None")
## ...     .having_other_terms_in_top(10)
## ...     .having_other_terms_ordered_by("OCC")
## ...     .having_other_term_occurrences_between(2, None)
## ...     .having_other_term_citations_between(None, None)
## ...     .having_other_terms_in(None)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     #
## ...     .build()
## ... )
## >>> associations.head()
                              FINTECH 31:5168
rows                                         
INNOVATION 07:0911                          5
FINANCIAL_SERVICES 04:0667                  3
FINANCIAL_INCLUSION 03:0590                 3
MARKETPLACE_LENDING 03:0317                 3
FINANCIAL_TECHNOLOGY 03:0461                2


"""

from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.item_params import ItemParams
from .internals.analysis_params import AnalysisParams, AnalysisParamsMixin


class DataFrame(
    AnalysisParamsMixin,
    ColumnsAndRowsParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.analysis_params = AnalysisParams()
        self.columns_params = ItemParams()
        self.database_params = DatabaseFilters()
        self.rows_params = ItemParams()

    def build(self):

        def extract_item_position_and_name(candidate_items, item):
            """Obtains the positions of topics in a list."""

            org_candidate_items = candidate_items[:]
            candidate_items = [col.split(" ")[:-1] for col in candidate_items]
            candidate_items = [" ".join(col) for col in candidate_items]
            pos = candidate_items.index(item)
            name = org_candidate_items[pos]
            return pos, name

        def extract_item_column_from_coc_matrix(obj, pos, name):
            matrix = obj.copy()
            series = matrix.iloc[:, pos]
            series = series.drop(labels=[name], axis=0, errors="ignore")
            series.index.name = obj.index.name
            return series

        #
        #
        # MAIN CODE:
        #
        #
        cooc_matrix = (
            CrossCoOccurrenceMatrix()
            .set_columns_params(**self.columns_params.__dict__)
            .set_rows_params(**self.rows_params.__dict__)
            .set_database_params(**self.database_params.__dict__)
            .build()
        )

        pos, name = extract_item_position_and_name(
            cooc_matrix.columns, self.analysis_params.item
        )
        series = extract_item_column_from_coc_matrix(cooc_matrix, pos, name)
        frame = series.to_frame()
        frame["OCC"] = [text.split(" ")[-1].split(":")[0] for text in frame.index]
        frame["GC"] = [text.split(" ")[-1].split(":")[-1] for text in frame.index]
        frame["NAME"] = [" ".join(text.split(" ")[:-1]) for text in frame.index]
        frame = frame.sort_values(
            by=[name, "OCC", "GC", "NAME"], ascending=[False, False, False, True]
        )
        frame = frame[[name]]

        return frame
