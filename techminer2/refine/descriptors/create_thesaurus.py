"""
CreateThesaurus
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.refine.descriptors import CreateThesaurus
    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("tests/data/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : ...fintech-with-references/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2467 items added to the thesaurus.
    <BLANKLINE>


"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2.refine._internals.objs import ThesaurusCreationResult

from ..user.create_thesaurus import CreateThesaurus as UserCreateThesaurus


class CreateThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> ThesaurusCreationResult:
        """:meta private:"""

        return (
            UserCreateThesaurus()
            .using_colored_output(self.params.colored_output)
            .with_source_field(CorpusField.KEY_AND_NP_AND_WORDS)
            .with_thesaurus_file("descriptors.the.txt")
            .where_root_directory(self.params.root_directory)
            .run()
        )
