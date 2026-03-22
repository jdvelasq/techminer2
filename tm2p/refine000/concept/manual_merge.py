"""
MergeKeys
===============================================================================

Smoke tests:
    >>> from tm2p import Field
    >>> from tm2p.refine.descriptors import CreateThesaurus
    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/tests/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2441 items added to the thesaurus.
    <BLANKLINE>



    >>> from tm2p.refine.descriptors import MergeKeys
    >>> (
    ...     MergeKeys()
    ...     .having_preferred_key("fintech")
    ...     .having_variant_keys(("financial technology", "financial technologies"))
    ...     .where_root_directory("tests/scopus/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )



"""

from tm2p import Field, ThField
from tm2p._intern import ParamsMixin
from tm2p.refine000.usr.merge_keys import MergeKeys as UserMergeKeys

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


class MergeKeys(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserMergeKeys()
            .update(**self.params.__dict__)
            .with_thesaurus_file("concepts.the.txt")
            .with_source_field(Field.CONCEPT_RAW)
            .run()
        )
