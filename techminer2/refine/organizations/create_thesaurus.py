"""
CreateThesaurus
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.refine.organizations import CreateThesaurus
    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/small/refine/thesaurus/organizations.the.txt
      Source field : ORGANIZATION_AND_AFFIL
      Status       : 45 organizations added to the thesaurus.
    <BLANKLINE>



"""

from pathlib import Path

from tqdm import tqdm  # type: ignore

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_main_data
from techminer2.refine._internals.objs import ThesaurusCreationResult

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
            usecols=[CorpusField.ORGANIZATION_AND_AFFIL.value],
        )
        dataframe = dataframe.dropna()
        series = dataframe[CorpusField.ORGANIZATION_AND_AFFIL.value]
        series = series.str.split("; ")
        series = series.explode()
        series = series.str.strip()
        series = series.drop_duplicates()
        series = series.str.split(" @ ")
        terms = series.to_list()

        mapping: dict[str, list[str]] = {}

        for term in terms:
            if term == ["[N/A]"]:
                continue
            organization, affil = term
            if organization not in mapping:
                mapping[organization] = []
            mapping[organization].append(affil)

        filepath = (
            Path(self.params.root_directory)
            / "refine"
            / "thesaurus"
            / "organizations.the.txt"
        )

        with open(filepath, "w", encoding="utf-8") as file:
            for organization in sorted(mapping.keys()):
                file.write(f"{organization}\n")
                for affil in sorted(mapping[organization]):
                    file.write(f"    {affil}\n")

        return ThesaurusCreationResult(
            colored_output=self.params.colored_output,
            file_path=str(filepath),
            source_field=CorpusField.ORGANIZATION_AND_AFFIL.value,
            msg="Thesaurus initialized successfully.",
            success=True,
            status=f"{len(mapping.keys())} organizations added to the thesaurus.",
        )
