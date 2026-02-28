"""
StartsWithExtractor
===============================================================================

Smoke tests:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.extract import StartsWithExtractor
    >>> terms = (
    ...     StartsWithExtractor()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # SEARCH:
    ...     .having_text_matching("finan")
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
    ['financial globalization',
     'financial inclusion',
     'financial information market',
     'financial innovation',
     'financial institution',
     'financial institution strategy',
     'financial instruments',
     'financial regulation',
     'financial scenarization',
     'financial services']


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.startswith import extract_startswith


class StartsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_startswith(self.params)


#
