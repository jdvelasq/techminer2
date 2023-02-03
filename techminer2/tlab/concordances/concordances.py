"""
Concordances
=========================================================================================

Abstract concordances exploration tool.


>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> tlab.concordances.concordances(
...     'regtech',
...     top_n=10,
...     directory=directory,
... )
<<< l systems requires increasing the use of and reliance on REGTECH .
                                                             REGTECH developments are leading towards a paradigm shift necess >>>
                                                             REGTECH to date has focused on the digitization of manual report >>>
                                   However, the potential of REGTECH is far greater  it has the potential to enable a nearly  >>>
<<< ld, sets the foundation for a practical understanding of REGTECH , and proposes sequenced reforms that could benefit regu >>>
<<< s the promise and potential of regulatory technologies ( REGTECH ), a new and vital dimension to fintech.
<<<  five-year research programme to highlight the role that REGTECH can play in making regulatory compliance more efficient  >>>
<<< emantically enabled applications can be made possible by REGTECH .
                 The chapter notes that the full benefits of REGTECH will only materialise if the pitfalls of a fragmented to >>>
           Although also not a panacea, the development of " REGTECH " solutions will help clear away volumes of work that un >>>


"""
import os.path
import textwrap

from ..._load_abstracts import load_abstracts
from ..._read_records import read_records


def concordances(
    search_for,
    top_n=50,
    quiet=False,
    directory="./",
    start_year=None,
    end_year=None,
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    records = read_records(
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    abstracts = load_abstracts(directory)
    abstracts = abstracts[abstracts.article.isin(records.article)]
    abstracts = abstracts.sort_values(
        ["global_citations", "article", "line_no"], ascending=[False, True, True]
    )
    abstracts = _select_abstracts(abstracts, search_for)

    _write_report(directory, abstracts, start_year, end_year, **filters)

    if not quiet:
        abstracts = abstracts.head(top_n)
        contexts = _extract_contexts(abstracts, search_for)
        _print_concordances(contexts, search_for)


def _write_report(directory, abstracts, start_year, end_year, **filters):

    abstracts = abstracts.copy()
    abstracts = abstracts[["global_citations", "article", "phrase"]]
    abstracts = abstracts.groupby(["article"], as_index=False).agg(list)
    abstracts["phrase"] = abstracts["phrase"].str.join("  ")
    abstracts["global_citations"] = abstracts["global_citations"].map(max)
    abstracts = abstracts.sort_values("global_citations", ascending=False)

    records = read_records(
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    records.index = records.article
    abstracts.index = abstracts.article
    abstracts["title"] = records.loc[abstracts.article, "title"]

    file_name = os.path.join(directory, "reports", "concordances.txt")
    with open(file_name, "w", encoding="utf-8") as out_file:
        counter = 0

        for _, row in abstracts.iterrows():
            print("-- {:03d} ".format(counter) + "-" * 83, file=out_file)
            print("AR ", end="", file=out_file)
            print(_fill(row["article"]), file=out_file)
            print("TI ", end="", file=out_file)
            print(_fill(row["title"]), file=out_file)
            print("TC ", end="", file=out_file)
            print(str(row.global_citations), file=out_file)
            print("AB ", end="", file=out_file)
            print(_fill(row.phrase), file=out_file)
            print("\n", file=out_file)

            counter += 1


def _fill(text):
    if isinstance(text, str):
        return textwrap.fill(
            text,
            width=87,
            initial_indent=" " * 0,
            subsequent_indent=" " * 3,
            fix_sentence_endings=True,
        )
    else:
        return ""


def _print_concordances(contexts, text):
    """Prints the report."""
    for _, row in contexts.iterrows():
        print(f"{row['left_context']:>60} {text.upper()} {row['right_context']}")


def _extract_contexts(abstracts, text):
    text = text.upper()
    regex = r"\b" + text + r"\b"
    contexts = abstracts["phrase"].str.extract(
        r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)"
    )

    contexts["left_context"] = contexts["left_context"].fillna("")
    contexts["left_context"] = contexts["left_context"].str.strip()

    contexts["right_context"] = contexts["right_context"].fillna("")
    contexts["right_context"] = contexts["right_context"].str.strip()
    contexts["left_context"] = contexts["left_context"].map(
        lambda x: "<<< " + x[-56:] if len(x) > 60 else x
    )
    contexts["right_context"] = contexts["right_context"].map(
        lambda x: x[:56] + " >>>" if len(x) > 60 else x
    )
    return contexts


def _select_abstracts(abstracts, text):
    """Selects the abstracts."""

    regex = r"\b" + text + r"\b"
    abstracts = abstracts[abstracts.phrase.str.contains(regex, regex=True)]
    abstracts["phrase"] = abstracts["phrase"].str.capitalize()
    abstracts["phrase"] = abstracts["phrase"].str.replace(
        r"\b" + text + r"\b", text.upper(), regex=True
    )
    abstracts["phrase"] = abstracts["phrase"].str.replace(
        r"\b" + text.capitalize() + r"\b", text.upper(), regex=True
    )

    return abstracts
