"""
CreateThesaurus
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.refine.user import CreateThesaurus
    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .with_source_field(CorpusField.DESCRIPTOR_TOK)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/small/refine/thesaurus/descriptors.the.txt
      Source field : DESCRIPTOR_TOK
      Status       : 2494 items add to the thesaurus.
    <BLANKLINE>



"""

from pathlib import Path

from tqdm import tqdm  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_main_data
from techminer2.refine.user._internals import ThesaurusCreationResult

tqdm.pandas()


class CreateThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def run(self) -> ThesaurusCreationResult:
        """:meta private:"""

        dataframe = load_main_data(
            root_directory=self.params.root_directory,
            usecols=[self.params.source_field.value],
        )
        dataframe = dataframe.dropna()
        series = dataframe[self.params.source_field.value]
        series = series.str.split("; ")
        series = series.explode()
        series = series.str.strip()
        series = series.drop_duplicates()
        terms = series.to_list()
        terms = sorted(terms)

        filepath = (
            Path(self.params.root_directory)
            / "refine"
            / "thesaurus"
            / "descriptors.the.txt"
        )

        with open(filepath, "w", encoding="utf-8") as file:
            for term in terms:
                file.write(f"{term}\n")
                file.write(f"    {term}\n")

        return ThesaurusCreationResult(
            colored_output=self.params.colored_output,
            file_path=str(filepath),
            source_field=self.params.source_field.value,
            msg="Thesaurus initialized successfully.",
            success=True,
            status=f"{len(terms)} items add to the thesaurus.",
        )
