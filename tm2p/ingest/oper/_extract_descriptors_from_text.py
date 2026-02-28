"""
Extract Descriptors from Text
===============================================================================


## >>> from tm2p.database.search import extract_descriptors_from_text
## >>> extract_descriptors_from_text(
## ...    text = (
## ...        "They highlight the limited adoption of Regulatory Technology (RegTech) and "
## ...        "Electronic Signatures in Palestine's banking sector, proposing the establishment "
## ...        "of an independent Electronic Transactions Unit as a solution. They emphasize the "
## ...        "need for RegTech in achieving regulatory compliance, risk management, and reporting "
## ...        "in the face of changing regulations and digital dynamics. Additionally, the papers "
## ...        "delve into ethical concerns surrounding the application of Artificial Intelligence (AI) "
## ...        "in finance and suggest that RegTech, combined with Islamic finance principles, can "
## ...        "mitigate these ethical issues. Overall, the papers underscore the transformative "
## ...        "potential of RegTech while discussing its benefits, challenges, and implications "
## ...        "for diverse sectors, ultimately aiming to improve compliance, efficiency, and ethical "
## ...        "practices in the financial industry."
## ...     ),
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/",
## ... ) # doctest: +ELLIPSIS
['ADOPTION', 'ARTIFICIAL_INTELLIGENCE', 'FINANCE', ...

"""

# import os.path
# import re

# from textblob import TextBlob  # type: ignore

# from tm2p.refine.thesaurus_old._internals.load_reversed_thesaurus_as_mapping import (
#     internal__load_reversed_thesaurus_as_mapping,
# )

# TEXTWRAP_WIDTH = 73
# THESAURUS_FILE = "data/thesaurus/descriptors.the.txt"


# def extract_descriptors_from_text(
#     text,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
# ):
#     """
#     :meta private:
#     """

#     #
#     # Obtains a regex for descriptors
#     thesaurus = load_thesaurus(root_dir)
#     descriptors = list(thesaurus.values())
#     descriptors = [d.translate(str.maketrans("_", " ")) for d in descriptors]
#     descriptors = [d.lower().strip() for d in descriptors]
#     descriptors = sorted(descriptors, key=lambda x: len(x.split(" ")), reverse=True)
#     descriptors = [re.escape(d) for d in descriptors]
#     descriptors = "|".join(descriptors)
#     regex = re.compile(r"\b(" + descriptors + r")\b")

#     #
#     # Highlight the text with the descriptors
#     text = text.lower().replace("_", " ")
#     text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

#     descriptors = sorted(set(str(t) for t in TextBlob(text).words))
#     descriptors = [
#         t for t in descriptors if t == t.upper() and t[0] not in "0123456789"
#     ]
#     return descriptors


# def load_thesaurus(root_dir):
#     th_file = os.path.join(root_dir, THESAURUS_FILE)
#     if not os.path.isfile(th_file):
#         raise FileNotFoundError(f"The file {th_file} does not exist.")
#     thesaurus = internal__load_reversed_thesaurus_as_mapping(th_file)
#     return thesaurus
