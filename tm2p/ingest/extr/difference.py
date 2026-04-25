"""
DifferenceExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import DifferenceExtractor
    >>> terms = (
    ...     DifferenceExtractor()
    ...     #
    ...     # FIELDS:
    ...     .with_source_fields(
    ...         (Field.AUTHKW_NORM, Field.IDXKW_NORM)
    ...     )
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert len(terms) > 0
    >>> from pprint import pprint
    >>> pprint(terms[:10])  # doctest: +SKIP
    ['130-nm process design kit ( pdk )',
     '1d convolutional neural network ( 1d-cnn )',
     '1d-cnn classifier',
     '21st century skills',
     '3d interaction',
     '5g battlefield networks',
     '5g networks',
     '6g iot networks',
     '6g networks',
     '6g-enabled v2x networks']


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
