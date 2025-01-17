# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ends With
===============================================================================

>>> from techminer2.database.field_extractors import EndsWithExtractor
>>> terms = (
...     EndsWithExtractor() 
...     .set_pattern("NING")
...     .set_field("author_keywords") 
...     .set_root_dir("example/")
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['RULE_LEARNING',
 'ORGANIZATIONAL_LEARNING',
 'COST_SENSITIVE_LEARNING',
 'DATA_MINING',
 'MACHINE_LEARNING',
 'METALEARNING',
 'ENTERPRISE_RESOURCE_PLANNING',
 'BOUNDARY_SPANNING',
 'LEARNING',
 'PROJECT_PLANNING']

"""


from ...internals.set_params_mixin.set_field_mixin import SetFieldMixin
from ...internals.set_params_mixin.set_pattern_mixin import SetPatternMixin
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ..internals.field_extractors.internal__ends_with import internal__ends_with


class EndsWithExtractor(
    SetFieldMixin,
    SetRootDirMixin,
    SetPatternMixin,
):
    """:meta private:"""

    def __init__(self):

        self.field = None
        self.pattern = None
        self.root_dir = "./"

    def build(self):

        return internal__ends_with(
            field=self.field,
            pattern=self.pattern,
            root_dir=self.root_dir,
        )
