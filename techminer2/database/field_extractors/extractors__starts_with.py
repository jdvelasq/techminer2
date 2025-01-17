# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Starts With
===============================================================================

>>> from techminer2.database.field_extractors import StartsWithExtractor
>>> terms = (
...     StartsWithExtractor() 
...     .set_pattern("FINAN")
...     .set_field("author_keywords") 
...     .set_root_dir("example/")
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['FINANCIAL_DEVELOPMENT',
 'FINANCIAL_MARKETS',
 'FINANCIAL_SERVICES',
 'FINANCIAL_SERVICES_NETWORK_EXTERNALITIES',
 'FINANCIAL_ECONOMICS',
 'FINANCIAL_SERVICES_INDUSTRY',
 'FINANCIAL_CRISES',
 'FINANCIAL_INTERMEDIATION',
 'FINANCIAL_RISK_MANAGEMENT',
 'FINANCE']

"""


from ...internals.set_params_mixin.set_field_mixin import SetFieldMixin
from ...internals.set_params_mixin.set_pattern_mixin import SetPatternMixin
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ..internals.field_extractors.internal__starts_with import internal__starts_with


class StartsWithExtractor(
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

        return internal__starts_with(
            field=self.field,
            pattern=self.pattern,
            root_dir=self.root_dir,
        )
