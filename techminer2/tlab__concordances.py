"""
Concordances (ok!)
=========================================================================================

Abstract concordances exploration tool.


>>> directory = "data/regtech/"

>>> from techminer2 import tlab__concordances
>>> tlab__concordances(
...     'regtech',
...     top_n=10,
...     directory=directory,
... )
<<< l systems requires increasing the use of and reliance on REGTECH .
                                                             REGTECH developments are leading towards a paradigm shift necess >>>
                                                             REGTECH to date has focused on the digitization of manual report >>>
                                   However, the potential of REGTECH is far greater  it has the potential to enable a nearly  >>>
<<< ld, sets the foundation for a practical understanding of REGTECH , and proposes sequenced reforms that could benefit regu >>>
           Although also not a panacea, the development of " REGTECH " solutions will help clear away volumes of work that un >>>
                                                             REGTECH will not eliminate policy considerations, nor will it re >>>
                 Nevertheless, a sophisticated deployment of REGTECH should help focus regulatory discretion and public-polic >>>
                                             Europes road to REGTECH has rested upon four apparently unrelated pillars: (1) e >>>
<<< that together they are underpinning the development of a REGTECH ecosystem in europe and will continue to do so.


"""
from ._load_abstracts import load_abstracts
from ._read_records import read_records


def tlab__concordances(
    search_for,
    top_n=50,
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
    abstracts = abstracts.head(top_n)
    contexts = _extract_contexts(abstracts, search_for)
    _print_concordances(contexts, search_for)


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
