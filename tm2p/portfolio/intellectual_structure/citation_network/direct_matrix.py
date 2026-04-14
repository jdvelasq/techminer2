"""
DirectMatrix
===============================================================================

* **CitationUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit
    >>> from tm2p.portfolio.intellectual_structure.citation_network import DirectMatrix
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> df = (
    ...     DirectMatrix()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.shape
    (109, 109)
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> df.iloc[0:10, 0:10].round(3)  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                         Arner DW 2020 1:00338  ...  Omarova ST 2020 1:00065
    ROWS                                                   ...
    Arner DW 2020 1:00338                             0.0  ...                      0.0
    Anagnostopoulos I 2018 1:00284                    0.0  ...                      0.0
    Zetzsche DA 2020 1:00222                          0.0  ...                      1.0
    Mirza N 2023 1:00112                              0.0  ...                      0.0
    Muganyi T 2022 1:00109                            0.0  ...                      0.0
    Lui A 2018 1:00096                                0.0  ...                      0.0
    Das SR 2019 1:00090                               0.0  ...                      0.0
    Sangwan V 2019 1:00082                            0.0  ...                      0.0
    Takeda A 2021 1:00066                             0.0  ...                      0.0
    Omarova ST 2020 1:00065                           0.0  ...                      0.0
    <BLANKLINE>
    [10 rows x 10 columns]



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.networks.normalize_matrix import normalize_matrix

from .matrix import Matrix


class DirectMatrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()

        matrix = normalize_matrix(
            association_index=self.params.association_index,
            matrix=matrix,
            params=self.params,
        )

        matrix.columns.name = "COLUMNS"
        matrix.index.name = "ROWS"

        return matrix
