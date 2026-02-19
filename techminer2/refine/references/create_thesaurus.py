"""
CreateThesaurus
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField
    >>> from techminer2.refine.references import CreateThesaurus
    >>> (
    ...     CreateThesaurus()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success      : True
      File         : examples/small/refine/thesaurus/references.the.txt
      Source field : REF_AND_REC_ID
      Status       : 57 references added to the thesaurus.
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
            usecols=[CorpusField.REF_AND_REC_ID.value],
        )
        dataframe = dataframe.dropna()
        series = dataframe[CorpusField.REF_AND_REC_ID.value]
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
            rec_id, ref = term
            if rec_id == "[N/A]":
                continue
            if rec_id not in mapping:
                mapping[rec_id] = []
            mapping[rec_id].append(ref)

        filepath = (
            Path(self.params.root_directory)
            / "refine"
            / "thesaurus"
            / "references.the.txt"
        )

        with open(filepath, "w", encoding="utf-8") as file:
            for rec_id in sorted(mapping.keys()):
                file.write(f"{rec_id}\n")
                for ref in sorted(mapping[rec_id]):
                    file.write(f"    {ref}\n")

        return ThesaurusCreationResult(
            colored_output=self.params.colored_output,
            file_path=str(filepath),
            source_field=CorpusField.REF_AND_REC_ID.value,
            msg="Thesaurus initialized successfully.",
            success=True,
            status=f"{len(mapping.keys())} references added to the thesaurus.",
        )
