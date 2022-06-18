"""
Abstract Screening
===============================================================================

Captures n-words around the keyword.


>>> from techminer2 import *
>>> directory = "data/"
>>> abstract_screening(
...     text='fintech',
...     top_n=10,
...     left=4,
...     right=4,
...     directory=directory,
... )
- INFO - Saved HTML report: data/reports/abstract_screening.html
                  industry overall, and many FINTECH start-ups are looking
                            hook up with the FINTECH revolution is at stake
                            We present a new FINTECH innovation mapping approach that
                influenced by blockchain and FINTECH innovations
 organisations, philanthropic investment and FINTECH companies
                         about what the term FINTECH means
                  explores the complexity of FINTECH, and attempts a definition
                     out the quintessence of FINTECH using both spheres
                        it is concluded that FINTECH is a new financial
                    Financial technology, or FINTECH, involves the design and

"""

from .abstract_concordances import _select_abstracts
from .load_abstracts import load_abstracts
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
        ["global_citations", "record_no", "line_no"], ascending=[False, True, True]
    )
    abstracts = _select_abstracts(abstracts, text)
    contexts = _extract_contexts(abstracts, text, left, right)
    _create_report(directory, abstracts)
    contexts = contexts.head(top_n)
    _print_contexts(contexts.text.tolist())


def _create_report(directory, abstracts):

    abstracts = abstracts.copy()
    abstracts = abstracts[["document_id", "phrase"]]
    abstracts = abstracts.groupby("document_id", as_index=False).aggregate(
        lambda x: " <br> ".join(x)
    )

    report_name = "abstract_screening.html"
    template = load_template(report_name)
    html = template.render(
        concordances=zip(abstracts.document_id.tolist(), abstracts.phrase.tolist())
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
