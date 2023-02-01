"""
Keyword Concordances
===============================================================================

Abstract concordances exploration tool.



# >>> directory = "data/regtech/"


# >>> from techminer2 import keyword_concordances
# >>> keyword_concordances(
# ...     'regtech', 
# ...     top_n=10, 
# ...     directory=directory,
# ... )
# --INFO-- Abstract concordances report generated.
# <<<  systems requires increasing the use of and reliance on  regtech .
#                                                              regtech  developments are leading towards a paradigm shift neces >>>
#                                                              regtech  to date has focused on the digitization of manual repor >>>
#                                   However, the potential of  regtech  is far greater  it has the potential to enable a nearly >>>
# <<< d, sets the foundation for a practical understanding of  regtech , and proposes sequenced reforms that could benefit regu >>>
#            Although also not a panacea, the development of " regtech " solutions will help clear away volumes of work that un >>>
#                                                              regtech  will not eliminate policy considerations, nor will it r >>>
#                 Nevertheless, a sophisticated deployment of  regtech  should help focus regulatory discretion and public-poli >>>
#                                             Europes road to  regtech  has rested upon four apparently unrelated pillars: (1)  >>>
# <<< hat together they are underpinning the development of a  regtech  ecosystem in europe and will continue to do so.

"""
import sys
import textwrap
from os.path import isfile, join

import pandas as pd

from .._read_records import read_records
from .._load_thesaurus_as_dict import load_thesaurus_as_dict


def keyword_concordances(
    keyword,
    top_n=50,
    directory="./",
):

    # ---< Sort abstracts by importance >------------------------------------------------
    documents = read_records(directory)
    article2citation = dict(zip(documents["article"], documents["global_citations"]))
    abstracts = pd.read_csv(join(directory, "processed", "abstracts.csv"))
    abstracts["citations"] = abstracts["article"].map(article2citation)
    abstracts = abstracts.sort_values(
        ["citations", "article", "line_no"], ascending=[False, True, True]
    )

    # ----< loads keywords >-------------------------------------------------------------
    thesaurus_file = join(directory, "processed", "keywords.txt")
    if isfile(thesaurus_file):
        th = load_thesaurus_as_dict(thesaurus_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    # extract keys for thesaurus
    reversed_th = {value: key for key, values in th.items() for value in values}
    th_keys = []

    th_keys.append(reversed_th[keyword])
    expanded_keywords = [text for key in th_keys for text in th[key]]

    # ---< Selects the abstracts >-------------------------------------------------------
    regex = [r"\b" + word + r"\b" for word in expanded_keywords]
    regex = "|".join(regex)
    abstracts = abstracts[abstracts.phrase.str.contains(regex, regex=True)]
    abstracts = abstracts[["article", "phrase"]]
    abstracts["phrase"] = abstracts["phrase"].str.capitalize()
    for word in expanded_keywords:
        abstracts["phrase"] = abstracts["phrase"].str.replace(
            r"\b" + word + r"\b", word.upper(), regex=True
        )
        abstracts["phrase"] = abstracts["phrase"].str.replace(
            r"\b" + word.capitalize() + r"\b", word.upper(), regex=True
        )

    # ---< Writes the report >-----------------------------------------------------------
    with open(join(directory, "keyword_concordances.txt"), "w") as out_file:

        for _, row in abstracts.iterrows():

            paragraph = textwrap.fill(
                row["phrase"],
                width=90,
            )
            document_id = documents[documents.article == row.article].article.tolist()[
                0
            ]

            print("*** " + document_id, file=out_file)
            print(paragraph, file=out_file)
            print("", file=out_file)

    sys.stdout.write("--INFO-- Abstract concordances report generated.\n")

    # ---< Display results >-------------------------------------------------------------
    expanded_keywords = [word.upper() for word in expanded_keywords]

    regex = [r"\b" + word + r"\b" for word in expanded_keywords]
    regex = "(" + "|".join(regex) + ")"
    contexts = abstracts["phrase"].str.extract(
        r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)"
    )

    contexts["left_context"] = contexts["left_context"].fillna("")
    contexts["right_context"] = contexts["right_context"].fillna("")
    contexts["left_context"] = contexts["left_context"].map(
        lambda x: "<<< " + x[-56:] if len(x) > 60 else x
    )
    contexts["right_context"] = contexts["right_context"].map(
        lambda x: x[:56] + " >>>" if len(x) > 60 else x
    )

    for _, row in contexts.head(top_n).iterrows():
        print(
            "{:>60s} {:s} {:s}".format(
                row["left_context"],
                keyword,
                row["right_context"],
            )
        )
