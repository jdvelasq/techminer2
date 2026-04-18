"""
MatrixList
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import MatrixList
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                           CITED_UNIT               CITING_UNIT  OCC
    0           Arner DW 2019 1:00045     Arner DW 2020 1:00338    1
    1         Buckley RP 2020 1:00037     Arner DW 2020 1:00338    1
    2         Omarova ST 2020 1:00065  Zetzsche DA 2020 1:00222    1
    3       Kavassalis P 2018 1:00026      Mirza N 2023 1:00112    1
    4  Anagnostopoulos I 2018 1:00284    Muganyi T 2022 1:00109    1
    5  Anagnostopoulos I 2018 1:00284     Takeda A 2021 1:00066    1
    6          Currie WL 2018 1:00043     Takeda A 2021 1:00066    1
    7              Lui A 2018 1:00096     Takeda A 2021 1:00066    1
    8             Yang D 2018 1:00043     Takeda A 2021 1:00066    1
    9          Baxter LG 2016 1:00030   Omarova ST 2020 1:00065    1


* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(1)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.shape
    (27, 27)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit

from ...._intern.helpers.check_database import check_database
from ._intern.doc import DocMatrixList
from ._intern.other import OtherMatrixList


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

        if self.params.analysis_unit == AnalysisUnit.DOC:
            matrix_list = DocMatrixList
        else:
            matrix_list = OtherMatrixList

        return matrix_list().update(**self.params.__dict__).run()
