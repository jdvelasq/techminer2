# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fields Intersection
===============================================================================

>>> from techminer2.database.field_extractors import FieldsIntersectionExtractor
>>> terms = (
...     FieldsIntersectionExtractor() 
...     .set_compare_field("author_keywords") 
...     .set_to_field("index_keywords")
...     .set_root_dir("example/")
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['ABAC',
 'ABNORMAL_RETURNS',
 'ACCEPTANCE',
 'ACCESS',
 'ACCESS_CONTROL',
 'ACTIVE_PARTICIPATION',
 'ACTIVITY_RECOGNITION',
 'ACTOR_NETWORK',
 'ACTOR_NETWORK_THEORY',
 'ACTUALIZATION']

"""


from ...internals.set_params_mixin.set_compare_field_mixin import SetCompareFieldMixin
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_to_field_mixin import SetToFieldMixin
from ..internals.field_extractors.internal__fields_intersection import (
    internal__fields_intersection,
)


class FieldsIntersectionExtractor(
    SetCompareFieldMixin,
    SetRootDirMixin,
    SetToFieldMixin,
):
    """:meta private:"""

    def __init__(self):

        self.compare_field = None
        self.root_dir = "./"
        self.to_field = None

    def build(self):

        return internal__fields_intersection(
            compare_field=self.compare_field,
            to_field=self.to_field,
            root_dir=self.root_dir,
        )
