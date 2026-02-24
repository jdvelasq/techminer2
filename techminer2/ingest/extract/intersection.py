"""
IntersectionExtractor
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.extract import IntersectionExtractor
    >>> terms = (
    ...     IntersectionExtractor()
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
    >>> # Print the first 10 extracted terms
    >>> from pprint import pprint
    >>> pprint(terms[:10])
    ['actor network theory',
     'alipay',
     'bank',
     'biometric authentication',
     'blockchain',
     'computer science',
     'computing curricula',
     'content analysis',
     'digitalization',
     'entrepreneurship']

"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.intersection import extract_intersection


class IntersectionExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_intersection(self.params)


#

#
#
