# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""
Combine Keys
===============================================================================

Example:
    >>> # Preparation
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Use
    >>> from techminer2.thesaurus.user import CombineKeys
    >>> df = (
    ...     CombineKeys()
    ...     #
    ...     # FIELD:
    ...     .with_field("descriptors")
    ...     .with_field_pattern('FINTECH')
    ...     .having_terms_in_top(30)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(2, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +SKIP
           rows                 columns  probability combine?
    3   FINTECH            TECHNOLOGIES        0.316       no
    6   FINTECH  FINANCIAL_TECHNOLOGIES        0.289       no
    8   FINTECH  THE_FINANCIAL_INDUSTRY        0.237       no
    13  FINTECH              REGULATORS        0.211       no
    23  FINTECH                   BANKS        0.184       no



"""

from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.co_occurrence_matrix import DataFrame as CoocDataFrame


class CombineKeys(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def compute_cooc_matrix(self):

        self.cooc_matrix = (
            CoocDataFrame().update(**self.params.__dict__)
            #
            # ROWS:
            ## .with_other_field(None)
            ## .having_other_terms_in_top(None)
            ## .having_other_terms_ordered_by(None)
            ## .having_other_term_occurrences_between(None, None)
            ## .having_other_term_citations_between(None, None)
            ## .having_other_terms_in(None)
            #
            # COUNTERS:
            .using_term_counters(True)
            #
            .run()
        )

        self.cooc_matrix = self.cooc_matrix.loc[
            self.cooc_matrix.rows.str.startswith(self.params.pattern + " ")
        ]

        self.cooc_matrix["rows_occ"] = self.cooc_matrix["rows"].apply(
            lambda x: int(x.split(" ")[1].split(":")[0]) if isinstance(x, str) else 0
        )

        self.cooc_matrix["columns_occ"] = self.cooc_matrix["columns"].apply(
            lambda x: int(x.split(" ")[1].split(":")[0]) if isinstance(x, str) else 0
        )

        self.cooc_matrix = self.cooc_matrix[
            self.cooc_matrix.rows_occ > self.cooc_matrix.columns_occ
        ]

        self.cooc_matrix

    # -------------------------------------------------------------------------
    def compute_probabilities(self):

        occ = self.cooc_matrix.iloc[0, 0]
        occ = occ.split(" ")[1].split(":")[0]
        occ = int(occ)

        self.cooc_matrix["probability"] = self.cooc_matrix["OCC"] / occ

        self.cooc_matrix["probability"] = self.cooc_matrix["probability"].round(3)
        self.cooc_matrix = self.cooc_matrix.sort_values(
            by="probability", ascending=False
        )

        self.cooc_matrix["combine?"] = self.cooc_matrix["probability"].apply(
            lambda x: "yes" if x > 0.5 else "no"
        )

    # -------------------------------------------------------------------------
    def format_final_output(self):

        self.cooc_matrix["rows"] = self.cooc_matrix["rows"].apply(
            lambda x: x.split(" ")[0]
        )
        self.cooc_matrix["columns"] = self.cooc_matrix["columns"].apply(
            lambda x: x.split(" ")[0]
        )
        self.cooc_matrix = self.cooc_matrix[
            ["rows", "columns", "probability", "combine?"]
        ]

    # -------------------------------------------------------------------------
    def run(self):

        self.compute_cooc_matrix()
        self.compute_probabilities()
        self.format_final_output()
        return self.cooc_matrix
