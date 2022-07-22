"""
Text Screening
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import tlab__text_screening
>>> tlab__text_screening(
...     search_for='regtech',
...     top_n=2,
...     directory=directory,
... )
--INFO-- Saved HTML report: data/regtech/reports/text_screening.html
<BLANKLINE>
*** Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINANC, AND INCL, VOL 1: CRYPTOCURR, FINTECH, INSURTECH, AND REGUL, P359
<BLANKLINE>
Regulatory technology or 'REGTECH' is the use of technology, particularly
information technology, in the context of regulatory monitoring, reporting and
compliance. REGTECH to date has focused on the digitization of manual reporting
and compliance processes, for example in the context of know-your-customer
requirements. this offers tremendous cost savings to the financial services
industry and regulators. however, the potential of REGTECH is far greater - it
could enable close to real-time monitoring and a proportionate regulatory regime
that addresses risk and facilitates more efficient regulatory compliance. we
argue that the transformative nature of technology will only be captured by a
new approach that sits at the nexus between data, digital identity, and
regulation. we seek to expose the inadequacy and lack of ambition of simply
digitizing analogue processes in a digital financial world. the development of
financial technology ('fintech'), rapid developments in emerging markets, and
the recent pro-active stance of regulators in developing regulatory sandboxes,
represent a unique combination of events, which could facilitate the transition
from one regulatory model to another. 2018 elsevier inc. all rights reserved.
<BLANKLINE>
<BLANKLINE>
*** Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373
<BLANKLINE>
Regulatory change and technological developments following the 2008 global
financial crisis are changing the nature of financial markets, services, and
institutions. at the juncture of these phenomena lies regulatory technology or
regtechthe use of technology, particularly information technology, in the
context of regulatory monitoring, reporting, and compliance. regulating rapidly
transforming financial systems requires increasing the use of and reliance on
REGTECH. whilst the principal regulatory objectives (e.g., financial stability,
prudential safety and soundness, consumer protection and market integrity, and
market competition and development) remain, their means of application are
increasingly inadequate. REGTECH developments are leading towards a paradigm
shift necessitating the reconceptualization of financial regulation. REGTECH to
date has focused on the digitization of manual reporting and compliance
processes. this offers tremendous cost savings to the financial services
industry and regulators. however, the potential of REGTECH is far greater  it
has the potential to enable a nearly real-time and proportionate regulatory
regime that identifies and addresses risk while facilitating more efficient
regulatory compliance. we argue that the transformative nature of technology
will only be captured by a new approach at the nexus of data, digital identity,
and regulation. this paper seeks to expose the inadequacy of digitizing analogue
processes in a digital financial world, sets the foundation for a practical
understanding of REGTECH, and proposes sequenced reforms that could benefit
regulators, industry, and entrepreneurs in the financial sector and other
industries. 2017. all rights reserved.
<BLANKLINE>
<BLANKLINE>


"""
import textwrap

from ._load_abstracts import load_abstracts
from .abstract_concordances import _select_abstracts
from .load_template import load_template
from .save_html_report import save_html_report


def tlab__text_screening(
    search_for,
    top_n=5,
    directory="./",
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    abstracts = load_abstracts(directory)
    abstracts = _join_phrases(abstracts)
    abstracts = _select_abstracts(abstracts, search_for)
    _create_report(directory, abstracts)
    abstracts = abstracts.head(top_n)
    _print_abstracts(abstracts)


def _join_phrases(abstracts):
    abstracts = abstracts.copy()
    abstracts = abstracts.sort_values(
        ["global_citations", "article", "line_no"], ascending=[False, True, True]
    )
    abstracts = abstracts.groupby(["article", "global_citations"], as_index=False).agg(
        list
    )
    # abstracts.phrase = abstracts.phrase.map(lambda x: [y.title() for y in x])
    abstracts.phrase = abstracts.phrase.str.join(" ")
    return abstracts


def _create_report(directory, abstracts):

    abstracts = abstracts.copy()
    abstracts = abstracts[["article", "phrase"]]
    abstracts = abstracts.groupby("article", as_index=False).aggregate(
        lambda x: " <br> ".join(x)
    )

    report_name = "text_screening.html"
    template = load_template(report_name)
    html = template.render(
        concordances=zip(abstracts.article.tolist(), abstracts.phrase.tolist())
    )
    save_html_report(directory, html, report_name)


def _print_abstracts(abstracts):
    print()
    for article, phrase in zip(abstracts.article, abstracts.phrase):
        print("*** " + article)
        print()
        print(textwrap.fill(phrase, width=80))
        print()
        print()
