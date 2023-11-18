# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-bramcbes
"""
Fuzzy Search 
===============================================================================


>>> from techminer2.refine.thesaurus.keywords import fuzzy_search
>>> fuzzy_search(
...     #
...     # SEARCH PARAMS:
...     patterns='INTELIGEN',
...     threshold=70,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
AGENDA
ARTIFICIAL_INTELLIGENCE
COST_SAVINGS
     COST_SAVINGS
     TREMENDOUS_COST_SAVINGS
CURRENT_AGENDA
DEPENDENT_VARIABLES
END
ENDEAVOURS
ENTREPRENEURIAL_ENDEAVOURS
FINTECH_LENDERS
     FINTECH_LENDERS
     FINTECH_LENDERS_CHARGE
     ONLINE_FINTECH_LENDERS
FINTECH_LENDERS_PENETRATE_AREAS
GENDER
INDEPENDENT_PARTIES
INSTRUMENT_DEPENDABILITY
INTELLIGENT_ALGORITHMS
INTELLIGENT_ROBOTS
LENDERS
LENDING
LENDINGCLUB
LENDINGCLUB_CONSUMER_PLATFORM
LENDINGCLUB_LOANS_INCREASES
MARKETPLACE_LENDING
ONLINE_VENDORS
P2P_LENDING
PEER_TO_PEER_LENDING
     PEER_TO_PEER
     PEER_TO_PEER_LENDING
     PEER_TO_PEER_NETWORKS
PRACTICAL_RECOMMENDATIONS
RECENT_TENDENCIES
RECENT_TRENDS
RECOMMENDATIONS
SOUND_POLICY_RECOMMENDATIONS
TREND
     TREND
     TRENDS





"""
import os.path

import pandas as pd
from fuzzywuzzy import process

from ...._common.thesaurus_lib import load_system_thesaurus_as_dict

THESAURUS_FILE = "thesauri/keywords.the.txt"


def fuzzy_search(
    #
    # SEARCH PARAMS:
    patterns,
    threshold=80,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")

    th_dict = load_system_thesaurus_as_dict(th_file)

    reversed_th = {value: key for key, values in th_dict.items() for value in values}

    pdf = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )

    pdf["text"] = pdf.text.str.replace("_", " ").str.lower()

    result = []

    if isinstance(patterns, str):
        patterns = [patterns]

    patterns = [pattern.lower() for pattern in patterns]

    for pattern in patterns:
        potential_matches = process.extract(pattern, pdf.text, limit=None)
        for potential_match in potential_matches:
            if potential_match[1] >= threshold:
                result.append(pdf[pdf.text.str.contains(potential_match[0])])

    if len(result) == 0:
        print("--INFO-- No matches found for the current thresold")
        return

    pdf = pd.concat(result)

    keys = pdf.key.drop_duplicates()

    findings = {key: th_dict[key] for key in sorted(keys)}

    # reorder the thesaurus to reflect the search
    for key in findings.keys():
        th_dict.pop(key)

    with open(th_file, "w", encoding="utf-8") as file:
        for key in sorted(findings.keys()):
            file.write(key + "\n")
            for item in findings[key]:
                file.write("    " + item + "\n")

        for key in sorted(th_dict.keys()):
            file.write(key + "\n")
            for item in th_dict[key]:
                file.write("    " + item + "\n")

    for key, items in sorted(findings.items()):
        print(key)
        if len(items) > 1:
            for item in sorted(items):
                print("    ", item)
