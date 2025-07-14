# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Apply Thesaurus
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> applier = (
    ...     ApplyThesaurus(use_colorama=False)
    ...     .where_root_directory_is("example/")
    ... )
    >>> applier.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_author_keywords
      Target field : author_keywords
      Application process completed successfully
    <BLANKLINE>
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_index_keywords
      Target field : index_keywords
      Application process completed successfully
    <BLANKLINE>
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_keywords
      Target field : keywords
      Application process completed successfully
    <BLANKLINE>
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_document_title_nouns_and_phrases
      Target field : document_title_nouns_and_phrases
      Application process completed successfully
    <BLANKLINE>
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_abstract_nouns_and_phrases
      Target field : abstract_nouns_and_phrases
      Application process completed successfully
    <BLANKLINE>
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_nouns_and_phrases
      Target field : nouns_and_phrases
      Application process completed successfully
    <BLANKLINE>
    Applying user thesaurus to database...
              File : example/data/thesaurus/descriptors.the.txt
      Source field : raw_descriptors
      Target field : descriptors
      Application process completed successfully
    <BLANKLINE>
    <BLANKLINE>



"""


from ...._internals.mixins import ParamsMixin
from ...user import ApplyThesaurus as ApplyUserThesaurus

PAIRS = [
    ("raw_author_keywords", "author_keywords"),
    ("raw_index_keywords", "index_keywords"),
    ("raw_keywords", "keywords"),
    ("raw_document_title_nouns_and_phrases", "document_title_nouns_and_phrases"),
    ("raw_abstract_nouns_and_phrases", "abstract_nouns_and_phrases"),
    ("raw_nouns_and_phrases", "nouns_and_phrases"),
    ("raw_descriptors", "descriptors"),
]


class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        for index, (raw_column, column) in enumerate(PAIRS):

            (
                ApplyUserThesaurus(quiet=self.params.quiet)
                .update(**self.params.__dict__)
                .with_thesaurus_file("descriptors.the.txt")
                .with_field(raw_column)
                .with_other_field(column)
                .where_root_directory_is(self.params.root_directory)
                .run()
            )
