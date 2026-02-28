"""
DifferenceExtractor
===============================================================================

Smoke tests:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.extract import DifferenceExtractor
    >>> terms = (
    ...     DifferenceExtractor()
    ...     #
    ...     # FIELDS:
    ...     .with_source_fields(
    ...         (CorpusField.AUTH_KEY_NORM, CorpusField.IDX_KEY_NORM)
    ...     )
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['alternative finance',
     'alternative lending',
     'bank 30',
     'banking',
     'banking innovations',
     'banking regulation',
     'bayesian estimation',
     'biometric',
     'china',
     'chinese telecom']

"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.difference import extract_difference


class DifferenceExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_difference(self.params)


#
