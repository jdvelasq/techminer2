# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with AND
===============================================================================

>>> from techminer2.database.field_extractors import StemmingAndExtractor
>>> terms = (
...     StemmingAndExtractor() 
...     .set_custom_items(["financial technology", "machine learning"]) 
...     .set_source_field("author_keywords")
...     .set_root_dir("example/")
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['MACHINE_LEARNING',
 'FINANCIAL_TECHNOLOGY',
 'FINANCIAL_SERVICES_IS_AND_TECHNOLOGY',
 'FINANCIAL_TECHNOLOGY (FINTECH)',
 'FINANCIAL_TECHNOLOGIES',
 'BIG_DATA_MACHINE_LEARNING']


"""


from ...internals.set_params_mixin.set_custom_items_mixin import SetCustomItemsMixin
from ...internals.set_params_mixin.set_root_dir_mixin import SetRootDirMixin
from ...internals.set_params_mixin.set_source_field_mixin import SetSourceFieldMixin
from ..internals.field_extractors.internal__stemming import internal__stemming_and


class StemmingAndExtractor(
    SetRootDirMixin,
    SetSourceFieldMixin,
    SetCustomItemsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.custom_items = None
        self.root_dir = "./"
        self.source_field = None

    def build(self):

        return internal__stemming_and(
            custom_items=self.custom_items,
            source_field=self.source_field,
            root_dir=self.root_dir,
        )
