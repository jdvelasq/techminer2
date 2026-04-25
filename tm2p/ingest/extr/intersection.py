"""
IntersectionExtractor
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.extr import IntersectionExtractor
    >>> items = (
    ...     IntersectionExtractor()
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
    >>> assert len(items) > 0
    >>> from pprint import pprint
    >>> pprint(items[:10])
    ['1-bit quantization',
     '1d convolutional neural network',
     '1d-cnn',
     '3d indoor localization',
     '3d object detection',
     '3d-modeling',
     '5g',
     '5g communication',
     '5g integration',
     '6g']

"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.extr._helpers.intersection import extract_intersection


class IntersectionExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return extract_intersection(self.params)


#

#
#
