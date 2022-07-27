"""
Record View
===============================================================================

VantagePoint / Record View

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__record_view
>>> vantagepoint__record_view(
...     criterion='author_keywords',
...     search_for='regtech',
...     records_length=2,
...     directory=directory,
... )
AR Anagnostopoulos I, 2018, J ECON BUS, V100, P7
TI Fintech and regtech: Impact on regulators and banks
AU Anagnostopoulos I
TC 110
SO Journal of Economics and Business
PY 2018
AB the purpose of this paper is to develop an insight and review the effect of fintech
   development against the broader environment in financial technology.  we further aim
   to offer various perspectives in order to aid the understanding of the disruptive
   potential of fintech, and its implications for the wider financial ecosystem.  by
   drawing upon very recent and highly topical research on this area this study
   examines the implications for financial institutions, and regulation especially when
   technology poses a challenge to the global banking and regulatory system.  it is
   driven by a wide-ranging overview of the development, the current state, and
   possible future of fintech.  this paper attempts to connect practitioner-led and
   academic research.  while it draws on academic research, the perspective it takes is
   also practice-oriented.  it relies on the current academic literature as well as
   insights from industry sources, action research and other publicly available
   commentaries.  it also draws on professional practitioners roundtable discussions,
   and think-tanks in which the author has been an active participant.  we attempt to
   interpret banking, and regulatory issues from a behavioural perspective.  the last
   crisis exposed significant failures in regulation and supervision.  it has made the
   financial market law and compliance a key topic on the current agenda.  disruptive
   technological change also seems to be important in investigating regulatory
   compliance followed by change.  we contribute to the current literature review on
   financial and digital innovation by new entrants where this has also practical
   implications.  we also provide for an updated review of the current regulatory
   issues addressing the contextual root causes of disruption within the financial
   services domain.  the aim here is to assist market participants to improve
   effectiveness and collaboration.  the difficulties arising from extensive regulation
   may suggest a more liberal and principled approach to financial regulation.
   disruptive innovation has the potential for welfare outcomes for consumers,
   regulatory, and supervisory gains as well as reputational gains for the financial
   services industry.  it becomes even more important as the financial services
   industry evolves.  for example, the preparedness of the regulators to instil culture
   change and harmonise technological advancements with regulation could likely achieve
   many desired outcomes.  such results range from achieving an orderly market growth,
   further aiding systemic stability and restoring trust and confidence in the
   financial system.  our action-led research results have implications for both
   research and practice.  these should be of interest to regulatory standard setters,
   investors, international organisations and other academics who are researching
   regulatory and competition issues, and their manifestation within the financial and
   social contexts.  as a perspective on a social construct, this study appeals to
   regulators and law makers, entrepreneurs, and investors who participate in
   technology applied within the innovative financial services domain.  it is also of
   interest to bankers who might consider fintech and strategic partnerships as a
   prospective, future strategic direction.1  2018 elsevier inc.
DE business models; financial services; fintech; future research direction; regtech;
   regulation
ID nan
------------------------------------------------------------------------------------------
AR Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7
TI Sustainability, FinTech and Financial Inclusion
AU Arner DW; Buckley RP; Zetzsche DA; Veidt R
TC 40
SO European Business Organization Law Review
PY 2020
AB we argue financial technology (fintech) is the key driver for financial inclusion,
   which in turn underlies sustainable balanced development, as embodied in the un
   sustainable development goals (sdgs). the full potential of fintech to support the
   sdgs may be realized with a progressive approach to the development of underlying
   infrastructure to support digital financial transformation.  our research suggests
   that the best way to think about such a strategy is to focus on four primary
   pillars.  the first pillar requires the building of digital identity, simplified
   account opening and e-kyc systems, supported by the second pillar of open
   interoperable electronic payments systems.  the third pillar involves using the
   infrastructure of the first and second pillars to underpin electronic provision of
   government services and payments.  the fourth pillardesign of digital financial
   markets and systemssupports broader access to finance and investment.  implementing
   the four pillars is a major journey for any economy, but one which has tremendous
   potential to transform not only finance but economies and societies, through
   fintech, financial inclusion and sustainable balanced development.  2020, t.m.c.
   asser press.
DE e-kyc; electronic payment infrastructure; financial inclusion; fintech; regtech;
   sustainability; sustainable development goals; sustainable investment
ID nan

"""
## VantagePoint / Record View
import textwrap

import numpy as np

from ._read_records import read_records


def vantagepoint__record_view(
    criterion,
    search_for,
    case=False,
    flags=0,
    regex=True,
    records_length=10,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Record View."""

    documents = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    contains = documents[criterion].str.contains(
        search_for, case=case, flags=flags, regex=regex
    )
    contains = contains.dropna()
    contains = contains[contains]
    documents = documents.loc[contains.index, :]

    column_list = []

    reported_columns = [
        "article",
        "title",
        "authors",
        "global_citations",
        "source_title",
        "year",
        "abstract",
        "raw_author_keywords",
        "raw_index_keywords",
    ]

    for criterion in reported_columns:

        if criterion in documents.columns:
            column_list.append(criterion)

    documents = documents[column_list]
    if "global_citations" in documents.columns:
        documents = documents.sort_values(by="global_citations", ascending=False)

    documents = documents.head(records_length)

    for index, row in documents.iterrows():

        for criterion in reported_columns:

            if criterion not in row.index:
                continue

            if row[criterion] is None:
                continue

            if criterion == "article":
                print("AR ", end="")
            if criterion == "title":
                print("TI ", end="")
            if criterion == "authors":
                print("AU ", end="")
            if criterion == "global_citations":
                print("TC ", end="")
            if criterion == "source_title":
                print("SO ", end="")
            if criterion == "year":
                print("PY ", end="")
            if criterion == "abstract":
                print("AB ", end="")
            if criterion == "raw_author_keywords":
                print("DE ", end="")
            if criterion == "author_keywords":
                print("DE ", end="")
            if criterion == "raw_index_keywords":
                print("ID ", end="")
            if criterion == "index_keywords":
                print("ID ", end="")

            print(
                textwrap.fill(
                    str(row[criterion]),
                    width=87,
                    initial_indent=" " * 3,
                    subsequent_indent=" " * 3,
                    fix_sentence_endings=True,
                )[3:]
            )

        if index != documents.index[-1]:
            print("-" * 90)
