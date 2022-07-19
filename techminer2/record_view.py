"""
Record View
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import record_view
>>> record_view(
...     'author_keywords', 
...     'regtech',
...     top_n=1,
...     directory=directory,
... )
               title : Fintech and regtech: Impact on regulators and banks
             authors : Anagnostopoulos I
    global_citations : 110
        source_title : Journal of Economics and Business
                year : 2018
            abstract : the purpose of this paper is to develop an insight and review the effect of fintech
                       development against the broader environment in financial technology.  we further aim to
                       offer various perspectives in order to aid the understanding of the disruptive potential of
                       fintech, and its implications for the wider financial ecosystem.  by drawing upon very
                       recent and highly topical research on this area this study examines the implications for
                       financial institutions, and regulation especially when technology poses a challenge to the
                       global banking and regulatory system.  it is driven by a wide-ranging overview of the
                       development, the current state, and possible future of fintech.  this paper attempts to
                       connect practitioner-led and academic research.  while it draws on academic research, the
                       perspective it takes is also practice-oriented.  it relies on the current academic
                       literature as well as insights from industry sources, action research and other publicly
                       available commentaries.  it also draws on professional practitioners roundtable discussions,
                       and think-tanks in which the author has been an active participant.  we attempt to interpret
                       banking, and regulatory issues from a behavioural perspective.  the last crisis exposed
                       significant failures in regulation and supervision.  it has made the financial market law
                       and compliance a key topic on the current agenda.  disruptive technological change also
                       seems to be important in investigating regulatory compliance followed by change.  we
                       contribute to the current literature review on financial and digital innovation by new
                       entrants where this has also practical implications.  we also provide for an updated review
                       of the current regulatory issues addressing the contextual root causes of disruption within
                       the financial services domain.  the aim here is to assist market participants to improve
                       effectiveness and collaboration.  the difficulties arising from extensive regulation may
                       suggest a more liberal and principled approach to financial regulation.  disruptive
                       innovation has the potential for welfare outcomes for consumers, regulatory, and supervisory
                       gains as well as reputational gains for the financial services industry.  it becomes even
                       more important as the financial services industry evolves.  for example, the preparedness of
                       the regulators to instil culture change and harmonise technological advancements with
                       regulation could likely achieve many desired outcomes.  such results range from achieving an
                       orderly market growth, further aiding systemic stability and restoring trust and confidence
                       in the financial system.  our action-led research results have implications for both
                       research and practice.  these should be of interest to regulatory standard setters,
                       investors, international organisations and other academics who are researching regulatory
                       and competition issues, and their manifestation within the financial and social contexts.
                       as a perspective on a social construct, this study appeals to regulators and law makers,
                       entrepreneurs, and investors who participate in technology applied within the innovative
                       financial services domain.  it is also of interest to bankers who might consider fintech and
                       strategic partnerships as a prospective, future strategic direction.1  2018 elsevier inc.
 raw_author_keywords : business models
                       financial services
                       fintech
                       future research direction
                       regtech
                       regulation

"""
import textwrap

import pandas as pd

from .read_records import read_records


def record_view(
    col,
    text,
    case=False,
    flags=0,
    regex=True,
    top_n=10,
    directory="./",
    database="documents",
):
    """Record View."""

    documents = read_records(directory=directory, database=database, use_filter=False)
    contains = documents[col].str.contains(text, case=case, flags=flags, regex=regex)
    contains = contains.dropna()
    contains = contains[contains]
    documents = documents.loc[contains.index, :]

    column_list = []

    reported_columns = [
        "title",
        "authors",
        "global_citations",
        "source_title",
        "year",
        "abstract",
        "raw_author_keywords",
        "raw_index_keywords",
    ]

    for col in reported_columns:

        if col in documents.columns:
            column_list.append(col)

    documents = documents[column_list]
    if "global_citations" in documents.columns:
        documents = documents.sort_values(by="global_citations", ascending=False)

    documents = documents.head(top_n)

    for index, row in documents.iterrows():

        for col in reported_columns:

            if col not in row.index:
                continue

            if col == "document_title":
                print("      document_title :", end="")
                print(
                    textwrap.fill(
                        row[col],
                        width=115,
                        initial_indent=" " * 23,
                        subsequent_indent=" " * 23,
                        fix_sentence_endings=True,
                    )[22:]
                )
                continue

            if col == "abstract":
                if not pd.isna(row[col]):
                    print("            abstract :", end="")
                    print(
                        textwrap.fill(
                            row[col],
                            width=115,
                            initial_indent=" " * 23,
                            subsequent_indent=" " * 23,
                            fix_sentence_endings=True,
                        )[22:]
                    )
                continue

            if col in [
                "raw_author_keywords",
                "author_keywords",
                "raw_index_keywords",
                "index_keywords",
            ]:
                keywords = row[col]
                if pd.isna(keywords):
                    continue
                keywords = keywords.split("; ")
                print(" {:>19} : {}".format(col, keywords[0]))
                for keyword in keywords[1:]:
                    print(" " * 23 + keyword)
                continue

            print(" {:>19} : {}".format(col, row[col]))

        if index != documents.index[-1]:
            print("-" * 120)
