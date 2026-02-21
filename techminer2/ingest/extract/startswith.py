"""
Starts With
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.extract import StartsWithExtractor
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
    ...     .where_root_directory("examples/tests/")
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

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers.startswith import extract_startswith


class StartsWithExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_startswith(self.params)


#
