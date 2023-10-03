# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _concordances_contexts:

Concordances Contexts
=========================================================================================

Abstract concordances exploration tool.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> contexts = tm2p.concordances_contexts(
...     search_for='REGTECH',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> print(contexts)
                                                             REGTECH can provide an invaluable tool, in a BUSINESS as usual E >>>
                                                             REGTECH developments are leading towards a paradigm shift necess >>>
                                                             REGTECH to date has focused on the DIGITIZATION of manual REPORT >>>
                                                             REGTECH will not eliminate policy considerations, nor will IT re >>>
           although also not a panacea, the DEVELOPMENT of " REGTECH " solutions will help clear away volumes of work that un >>>
<<< s the promise and potential of REGULATORY_TECHNOLOGIES ( REGTECH ), a new and vital dimension to FINTECH
<<< paper, the authors propose a novel, regular TECHNOLOGY ( REGTECH ) cum automated legal text approach for financial TRANSA >>>
                     2020 the authorsregulatory TECHNOLOGY ( REGTECH )
                                     REGULATORY_TECHNOLOGY ( REGTECH ) is an emerging TECHNOLOGY trend leveraging INFORMATION >>>
<<< llustrate the impact of adopting REGULATORY_TECHNOLOGY ( REGTECH ) INNOVATIONS in BANKS on MONEY_LAUNDERING prevention ef >>>
<<< rpose of this paper is to explore the solutions that AI, REGTECH and CHARITYTECH provide to charities in navigating the v >>>
                                                in contrast, REGTECH has recently brought great SUCCESS to financial COMPLIAN >>>
<<< the area of FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly improve FINANCIAL_DEVELOPMENT outcomes
<<< that together they are underpinning the DEVELOPMENT of a REGTECH ECOSYSTEM in EUROPE and will continue to do so
                                 an option is to incorporate REGTECH into the DIGITAL_TRANSFORMATION STRATEGY of a MANAGEMENT >>>
<<< egulator based SELF_ASSESSMENT checklist to establish if REGTECH best practice could improve the demonstration of GDPR_CO >>>
                 the chapter notes that the full BENEFITS of REGTECH will only materialise if the pitfalls of a fragmented to >>>
<<< ld, sets the foundation for a practical understanding of REGTECH , and proposes sequenced reforms that could BENEFIT regu >>>
                                   however, the potential of REGTECH is far greater  IT has the potential to enable a nearly  >>>
                        this paper explores the potential of REGTECH and the merit of incorporating IT into a SMART_TREASURY  >>>
<<< ral awareness concerning the ADOPTION and integration of REGTECH PLATFORMS for fighting MONEY_LAUNDERING
<<< ING through REGTECH and cost  and time-saving aspects of REGTECH , drive MONEY_LAUNDERING prevention effectiveness to a h >>>
                 nevertheless, a sophisticated deployment of REGTECH should help focus regulatory discretion and PUBLIC_POLIC >>>
<<< ndings provide specific insights about the deployment of REGTECH capabilities in BANKS in regional BANKING centers of mod >>>
<<< and regulators, and provided an ENVIRONMENT within which REGTECH can flourish
<<< l systems requires increasing the use of and reliance on REGTECH 
<<< ide insights for other societies in developing their own REGTECH ECOSYSTEMS in order to support more efficient, stable, i >>>
                                             europes road to REGTECH has rested upon four apparently unrelated pillars: (1) e >>>
<<<  five-year research programme to highlight the role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient  >>>
<<< otwithstanding the RISK_REDUCTIONS and cost savings that REGTECH can deliver
<<< emantically enabled applications can be made possible by REGTECH 


"""
import pandas as pd

from .._common._read_records import read_records
from .concordances_lib import get_context_phrases_from_records


def concordances_contexts(
    #
    # FUNCTION PARAMS:
    search_for: str,
    top_n: int,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    def create_contexts_table(
        context_phrases: pd.Series,
    ):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = context_phrases.str.extract(
            r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)"
        )

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[
            contexts["left_context"].map(lambda x: x != "")
            | contexts["right_context"].map(lambda x: x != "")
        ]

        return contexts

    def transform_context_table_to_contexts(
        contexts: pd.DataFrame,
    ):
        """Transforms the contexts table to a text."""

        contexts = contexts.copy()

        contexts["left_r"] = contexts["left_context"].str[::-1]

        contexts = contexts.sort_values(["left_r", "right_context"])

        contexts["left_context"] = contexts["left_context"].map(
            lambda x: "<<< " + x[-56:] if len(x) > 60 else x
        )
        contexts["right_context"] = contexts["right_context"].map(
            lambda x: x[:56] + " >>>" if len(x) > 60 else x
        )

        texts = []
        for _, row in contexts.iterrows():
            text = f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
            texts.append(text)

        return "\n".join(texts)

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    context_phrases = get_context_phrases_from_records(
        search_for=search_for, records=records, top_n=top_n
    )
    context_table = create_contexts_table(context_phrases)
    contexts = transform_context_table_to_contexts(context_table)

    return contexts
