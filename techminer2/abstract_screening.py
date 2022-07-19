"""
Abstract Screening
===============================================================================

Captures n-words around the keyword.



>>> directory = "data/regtech/"

>>> from techminer2 import abstract_screening
>>> abstract_screening(
...     text='fintech',
...     top_n=10,
...     left=4,
...     right=4,
...     directory=directory,
... )
--INFO-- Saved HTML report: data/regtech/reports/abstract_screening.html
                 review the effect of FINTECH development against the broader
          the disruptive potential of FINTECH, and its implications for
                                      FINTECH
           bankers who might consider FINTECH and strategic partnerships as
       We argue financial technology (FINTECH) is the key driver
                The full potential of FINTECH to support the sdgs
     economies and societies, through FINTECH, financial inclusion and sustainable
                  that many banks and FINTECH start-ups are investing
      co-operative collaboration with FINTECH start-ups on regulatory
       field of financial technology (FINTECH) and the different financial


"""

from ._load_abstracts import load_abstracts
from .abstract_concordances import _select_abstracts
from .load_template import load_template
from .save_html_report import save_html_report


def abstract_screening(
    text,
    left=4,
    right=4,
    top_n=50,
    directory="./",
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    abstracts = load_abstracts(directory)
    abstracts = abstracts.sort_values(
        ["global_citations", "article", "line_no"], ascending=[False, True, True]
    )
    abstracts = _select_abstracts(abstracts, text)
    contexts = _extract_contexts(abstracts, text, left, right)
    _create_report(directory, abstracts)
    contexts = contexts.head(top_n)
    _print_contexts(contexts.text.tolist())


def _create_report(directory, abstracts):

    abstracts = abstracts.copy()
    abstracts = abstracts[["article", "phrase"]]
    abstracts = abstracts.groupby("article", as_index=False).aggregate(
        lambda x: " <br> ".join(x)
    )

    report_name = "abstract_screening.html"
    template = load_template(report_name)
    html = template.render(
        concordances=zip(abstracts.article.tolist(), abstracts.phrase.tolist())
    )
    save_html_report(directory, html, report_name)


def _extract_contexts(abstracts, text, left, right):
    text = text.upper()
    regex = r"\b" + text + r"\b"

    left_context_regex = r"(?P<left_context>(?:\w+\W+){1," + str(left) + "})"
    right_context_regex = r"(?P<right_context>(?:\W+\w+){1," + str(right) + "})"
    contexts = abstracts["phrase"].str.extract(
        left_context_regex + regex + right_context_regex
    )
    contexts["left_context"] = contexts["left_context"].fillna("")
    contexts["right_context"] = contexts["right_context"].fillna("")
    left_max_len = max(contexts["left_context"].str.len())
    contexts["left_context"] = contexts["left_context"].str.rjust(left_max_len)
    contexts = contexts.assign(
        text=contexts.left_context + text + contexts.right_context
    )

    return contexts


def _print_contexts(texts):
    for text in texts:
        print(text)
