# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Find Similar Records
===============================================================================




>>> from techminer2.search import find_similar_phrases
>>> find_similar_phrases(
...     text=(
...         "whilst the PRINCIPAL_REGULATORY_OBJECTIVES (e.g., FINANCIAL_STABILITY, "
...         "PRUDENTIAL_SAFETY and soundness, CONSUMER_PROTECTION and MARKET_INTEGRITY, "
...         "and MARKET_COMPETITION and DEVELOPMENT) remain, their means of application "
...         "are increasingly inadequate."
...     ),
...     top_n=3,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
----------------------------------------------------------------------------------------------------
SIMILARITY: 1.0
AR: Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373
TI: fintech, regtech, and the reconceptualization of FINANCIAL_REGULATION
<BLANKLINE>
whilst the PRINCIPAL_REGULATORY_OBJECTIVES (e.g., FINANCIAL_STABILITY,
PRUDENTIAL_SAFETY and soundness, CONSUMER_PROTECTION and MARKET_INTEGRITY,
and MARKET_COMPETITION and development) remain, their means of application
are increasingly inadequate.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.21
AR: Campbell-Verduyn M, 2022, NEW POLIT ECON
TI: IMAGINARY_FAILURE: regtech in finance
<BLANKLINE>
we point to the need for developing wider imaginaries of
TECHNOLOGICAL_POSSIBILITIES for regulation in an increasingly
DIGITAL_WORLD.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.124
AR: Baxter LG, 2016, DUKE LAW J, V66, P567
TI: adaptive FINANCIAL_REGULATION and regtech: a CONCEPT_ARTICLE on REALISTIC_PROTECTION for victims of BANK_FAILURES
<BLANKLINE>
yet regulators face an increasingly COMPLEX_TASK in supervising
MODERN_FINANCIAL_INSTITUTIONS.
<BLANKLINE>

>>> find_similar_phrases(
...     text=(
...         "Butler (2019) emphasizes the importance of semantic standards in realizing "
...         "the full benefits of RegTech, as demonstrated by initiatives like the Bank "
...         "of England/FCA RegTech Sprint."
...     ),
...     top_n=3,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.338
AR: Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN, P300
TI: towards a SMART_REGULATORY_COMPLIANCE, the capabilities of REGTECH and SUPTECH
<BLANKLINE>
REGTECH and SUPTECH were discussed mostly in banking or FINANCIAL_RESEARCH.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.286
AR: Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19
TI: on the role of ontology based REGTECH for managing risk and COMPLIANCE_REPORTING in the age of REGULATION
<BLANKLINE>
it also examines the POTENTIAL_IMPACT_FINTECH has on the riskiness of banks
and proposes REGTECH as the solution.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.286
AR: Miglionico A, 2020, EUR BUS LAW REV, V31, P641
TI: automated regulation and supervision: the impact of REGTECH on BANKING_COMPLIANCE
<BLANKLINE>
REGULATORY_TECHNOLOGIES (REGTECH) are the NEW_PARADIGM of supervision and
compliance in the banking sector.
<BLANKLINE>



>>> text = (
...    "They highlight the limited adoption of Regulatory Technology (RegTech) and "
...    "Electronic Signatures in Palestine's banking sector, proposing the establishment "
...    "of an independent Electronic Transactions Unit as a solution. They emphasize the "
...    "need for RegTech in achieving regulatory compliance, risk management, and reporting "
...    "in the face of changing regulations and digital dynamics. Additionally, the papers "
...    "delve into ethical concerns surrounding the application of Artificial Intelligence (AI) "
...    "in finance and suggest that RegTech, combined with Islamic finance principles, can "
...    "mitigate these ethical issues. Overall, the papers underscore the transformative "
...    "potential of RegTech while discussing its benefits, challenges, and implications "
...    "for diverse sectors, ultimately aiming to improve compliance, efficiency, and ethical "
...    "practices in the financial industry."
... )
>>> text = text.split(".")
>>> for phrase in text:
...     print("=" * 100)
...     print(phrase.strip())
...     find_similar_phrases(
...         text=phrase.strip(),
...         top_n=5,
...         #
...         # DATABASE PARAMS:
...         root_dir="data/regtech/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...    )
====================================================================================================
They highlight the limited adoption of Regulatory Technology (RegTech) and Electronic Signatures in Palestine's banking sector, proposing the establishment of an independent Electronic Transactions Unit as a solution
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.401
AR: Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135
TI: REGTECH as an ANTITRUST_ENFORCEMENT_TOOL
<BLANKLINE>
associated with this has been the rise of REGULATORY_TECHNOLOGY (REGTECH)
in that sector.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.327
AR: Ghanem S, 2021, STUD COMPUT INTELL, V954, P139
TI: REGTECH and ELECTRONIC_SIGNATURE: opportunities and challenges in the palestinian banking sector
<BLANKLINE>
the most IMPORTANT_RECOMMENDATION_RELATES to the establishment of an
ELECTRONIC_TRANSACTIONS_UNIT as stipulated in the law and that it should be
independent.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.303
AR: Miglionico A, 2020, EUR BUS LAW REV, V31, P641
TI: automated regulation and supervision: the impact of REGTECH on BANKING_COMPLIANCE
<BLANKLINE>
REGULATORY_TECHNOLOGIES (REGTECH) are the NEW_PARADIGM of supervision and
compliance in the banking sector.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.303
AR: Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19
TI: on the role of ontology based REGTECH for managing risk and COMPLIANCE_REPORTING in the age of REGULATION
<BLANKLINE>
it also examines the POTENTIAL_IMPACT_FINTECH has on the riskiness of banks
and proposes REGTECH as the solution.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.267
AR: Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN, V2020-September, P112
TI: REGTECH: CASE_STUDIES of cooperation with BANKS in italy
<BLANKLINE>
methods/approach: today the literature about CASE_STUDY in REGTECH is not
proposing any solution of cooperation on the REGULATORY_FIELD in italy.
<BLANKLINE>
====================================================================================================
They emphasize the need for RegTech in achieving regulatory compliance, risk management, and reporting in the face of changing regulations and digital dynamics
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.433
AR: Firmansyah B, 2022, INT CONF INF TECHNOL SYST INN, P310
TI: a SYSTEMATIC_LITERATURE_REVIEW of REGTECH: TECHNOLOGIES, CHARACTERISTICS, and ARCHITECTURES
<BLANKLINE>
the TECHNOLOGY at REGTECH will bring all these elements together to achieve
REGULATORY_COMPLIANCE.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.375
AR: Anagnostopoulos I, 2018, J ECON BUS, V100, P7
TI: FINTECH and REGTECH: impact on regulators and banks
<BLANKLINE>
for example, the preparedness of the regulators to INSTIL_CULTURE change
and HARMONISE_TECHNOLOGICAL_ADVANCEMENTS with REGULATION could likely
achieve many desired outcomes.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.354
AR: Anagnostopoulos I, 2018, J ECON BUS, V100, P7
TI: FINTECH and REGTECH: impact on regulators and banks
<BLANKLINE>
DISRUPTIVE_TECHNOLOGICAL change also seems to be important in investigating
REGULATORY_COMPLIANCE followed by change.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.333
AR: Grassi L, 2022, J IND BUS ECON, V49, P441
TI: REGTECH in public and PRIVATE_SECTORS: the nexus between DATA, technology and REGULATION
<BLANKLINE>
higher REGULATORY_COMPLIANCE_REQUIREMENTS, fast and CONTINUOUS_CHANGES in
regulations and HIGH_DIGITAL_DYNAMICS in the FINANCIAL_MARKETS are powering
REGTECH (REGULATORY_TECHNOLOGY), defined as technologyenabled innovation
applied to the world of REGULATION, COMPLIANCE, RISK_MANAGEMENT, REPORTING
and supervision.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.306
AR: Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382
TI: determinants for the adoption of REGULATORY_TECHNOLOGY (REGTECH) services by the companies in UNITED_ARAB_EMIRATES: an MCDM_APPROACH
<BLANKLINE>
the need for REGTECH's determinants would help FINANCIAL_INSTITUTIONS,
regulators, and stakeholders in the UAE_BENEFIT from the research and
achieve COMPETITIVE_ADVANTAGE by understanding and implementing the
suggested findings.
<BLANKLINE>
====================================================================================================
Additionally, the papers delve into ethical concerns surrounding the application of Artificial Intelligence (AI) in finance and suggest that RegTech, combined with Islamic finance principles, can mitigate these ethical issues
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.306
AR: Rabbani MR, 2022, LECT NOTES NETWORKS SYST, V423 LNNS, P381
TI: ethical concerns in ARTIFICIAL_INTELLIGENCE (ai): the role of regtech and ISLAMIC_FINANCE
<BLANKLINE>
this STUDY_ATTEMPTS to identify the ETHICAL_ISSUES in the application of
ARTIFICIAL_INTELLIGENCE and offers remedies from the SHARIAH_PRINCIPLES.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.218
AR: Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN, P300
TI: towards a SMART_REGULATORY_COMPLIANCE, the capabilities of REGTECH and SUPTECH
<BLANKLINE>
this paper also concludes the definition of REGTECH/SUPTECH and states one
CORE_CAPABILITY of REGTECH with its four pillars.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.218
AR: Firmansyah B, 2022, INT CONF INF TECHNOL SYST INN, P310
TI: a SYSTEMATIC_LITERATURE_REVIEW of REGTECH: TECHNOLOGIES, CHARACTERISTICS, and ARCHITECTURES
<BLANKLINE>
although dominant in the FINANCIAL_SECTOR, ideally, REGTECH can be
implemented in VARIOUS_SECTORS other than FINANCE.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.204
AR: Rabbani MR, 2022, LECT NOTES NETWORKS SYST, V423 LNNS, P381
TI: ethical concerns in ARTIFICIAL_INTELLIGENCE (ai): the role of regtech and ISLAMIC_FINANCE
<BLANKLINE>
the findings of the study suggest that the there is a
SIGNIFICANT_RELATIONSHIP between ETHICAL_ISSUES in AI_IMPLEMENTATION, role
of regtech and ISLAMIC_FINANCE.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.204
AR: Firmansyah B, 2022, INT CONF INF TECHNOL SYST INN, P310
TI: a SYSTEMATIC_LITERATURE_REVIEW of REGTECH: TECHNOLOGIES, CHARACTERISTICS, and ARCHITECTURES
<BLANKLINE>
VARIOUS_TECHNOLOGIES are used in REGTECH, such as BIG_DATA_ANALYTICS,
ARTIFICIAL_INTELLIGENCE, MACHINE_LEARNING, cloud computing, blockchain,
etc.
<BLANKLINE>
====================================================================================================
Overall, the papers underscore the transformative potential of RegTech while discussing its benefits, challenges, and implications for diverse sectors, ultimately aiming to improve compliance, efficiency, and ethical practices in the financial industry
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.25
AR: Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135
TI: REGTECH as an ANTITRUST_ENFORCEMENT_TOOL
<BLANKLINE>
associated with this has been the rise of REGULATORY_TECHNOLOGY (REGTECH)
in that sector.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.236
AR: Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801
TI: corporate whistleblowing, SMART_REGULATION and regtech: the coming of the whistlebot?
<BLANKLINE>
while first GENERATION_REGTECH_APPLICATIONS such as improved DATA_ANALYTICS
already have the capability to assist corporations to implement more
efficient internal whistleblowing systems, the rise of second generation ai
powered REGTECH_TECHNOLOGIES is likely to further disrupt, and potentially
transform, the practice of whistleblowing in corporations.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.224
AR: Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN, P300
TI: towards a SMART_REGULATORY_COMPLIANCE, the capabilities of REGTECH and SUPTECH
<BLANKLINE>
REGTECH and SUPTECH were discussed mostly in banking or FINANCIAL_RESEARCH.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.224
AR: Anagnostopoulos I, 2018, J ECON BUS, V100, P7
TI: FINTECH and REGTECH: impact on regulators and banks
<BLANKLINE>
our action led RESEARCH_RESULTS have implications for both research and
practice.
<BLANKLINE>
----------------------------------------------------------------------------------------------------
SIMILARITY: 0.208
AR: Nasir F, 2019, J ADV RES DYN CONTROL SYST, V11, P912
TI: REGTECH as a solution for COMPLIANCE_CHALLENGE: a REVIEW_ARTICLE
<BLANKLINE>
the purpose of this paper is to present a SYSTEMATIC_LITERATURE_REVIEW
conducted, on applying REGTECH to reduce COMPLIANCE_COST and burden, while
focusing on PROMISING_REGTECH_TOOLS and VARIOUS_BENEFITS and challenges of
REGTECH.
<BLANKLINE>
====================================================================================================
<BLANKLINE>




"""
import os
import os.path
import re
import textwrap

import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

from .._read_records import read_records
from ..thesaurus_lib import load_system_thesaurus_as_dict_reversed

TEXTWRAP_WIDTH = 75
THESAURUS_FILE = "words.txt"


def find_similar_phrases(
    text,
    top_n=5,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """
    :meta private:
    """

    if text.strip() == "":
        return

    #
    # Prepare abstracts

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = extract_sentences(records)
    records = remove_stopwords(records)
    records = apply_thesaurus_to_abstract(root_dir, records)
    records = remove_duplicated_words(records)
    records = apply_porter_stemmer(records)

    records["phrase_no"] = range(len(records))
    tf_matrix = records.explode("abstract")
    tf_matrix = build_tf_matrix(tf_matrix)

    #
    # Prepare text
    words = prepare_text(root_dir, text)
    words = apply_thesaurus_to_text(root_dir, words)
    words = [w for w in words if w in tf_matrix.columns]

    df_text = pd.DataFrame(data=[[0] * len(tf_matrix.columns)], columns=tf_matrix.columns)
    for word in words:
        df_text[word] = 1

    similarity = cosine_similarity(tf_matrix, df_text)
    similarity = [s[0] for s in similarity]
    records["similarity"] = similarity

    records = records.sort_values(by="similarity", ascending=False)
    records = records[records["similarity"] > 0.0]

    for _, row in records.head(top_n).iterrows():
        print("-" * 100)
        print("SIMILARITY: " + str(round(row.similarity, 3)))
        print("AR: " + row.article)
        print("TI: " + row.title)
        print()
        print(textwrap.fill(str(row.phrase), width=TEXTWRAP_WIDTH))
        print()


def apply_thesaurus_to_text(root_dir, words):
    """
    :meta private:
    """
    thesaurus = load_thesaurus(root_dir)
    words = [thesaurus[w] if w in thesaurus else w for w in words]
    return words


def load_thesaurus(root_dir):
    th_file = os.path.join(root_dir, THESAURUS_FILE)
    if not os.path.isfile(th_file):
        raise FileNotFoundError(f"The file {th_file} does not exist.")
    thesaurus = load_system_thesaurus_as_dict_reversed(th_file)
    return thesaurus


def prepare_text(root_dir, text):
    """
    :meta private:
    """

    #
    # Obtains a regex for descriptors
    thesaurus = load_thesaurus(root_dir)
    descriptors = list(thesaurus.values())
    descriptors = [d.translate(str.maketrans("_", " ")) for d in descriptors]
    descriptors = [d.lower().strip() for d in descriptors]
    descriptors = sorted(descriptors, key=lambda x: len(x.split(" ")), reverse=True)
    descriptors = [re.escape(d) for d in descriptors]
    descriptors = "|".join(descriptors)
    regex = re.compile(r"\b(" + descriptors + r")\b")

    #
    # Highlight the text with the descriptors
    text = text.lower().replace("_", " ")
    text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

    #
    # Obtain the words in the phase
    words = TextBlob(text).sentences[0].words

    #
    # Load and prepare the stopwords
    stopwords = load_stopwords()
    stopwords = [word.lower() for word in stopwords]

    words = [w for w in words if w not in stopwords]
    words = [w for w in words if w[0] not in "0123456789"]
    words = [w.replace("'", "") for w in words]
    words = [w for w in words if len(w) > 2]

    #
    # Apply Porter Stemmer
    stemmer = PorterStemmer()
    words = sorted(set(stemmer.stem(word) if word == word.lower() else word for word in words))

    return words


def apply_thesaurus_to_abstract(root_dir, records):
    """
    :meta private:
    """
    thesaurus = load_thesaurus(root_dir)
    records["abstract"] = records["abstract"].apply(
        lambda words: [thesaurus[w] if w in thesaurus else w for w in words]
    )
    return records


def apply_porter_stemmer(records):
    """
    :meta private:
    """
    stemmer = PorterStemmer()
    records["abstract"] = records["abstract"].apply(
        lambda x: sorted(set(stemmer.stem(w) if w == w.lower() else w for w in x))
    )
    return records


def build_tf_matrix(records):
    """
    :meta private:
    """
    records = records.copy()
    records["OCC"] = 1
    records = records.pivot(index="phrase_no", columns="abstract", values="OCC")
    records = records.fillna(0)
    return records


def remove_duplicated_words(records):
    """
    :meta private:
    """
    records["abstract"] = records["abstract"].apply(lambda x: sorted(set(x)))
    return records


def load_stopwords():
    """
    :meta private:
    """
    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "../word_lists/stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]
    return stopwords


def remove_stopwords(records):
    """
    :meta private:
    """
    stopwords = load_stopwords()
    stopwords = [word.lower() for word in stopwords]
    records["abstract"] = records["abstract"].apply(
        lambda words: [w for w in words if w not in stopwords]
    )

    records["abstract"] = records["abstract"].apply(
        lambda words: [w for w in words if w[0] not in "0123456789"]
    )

    records["abstract"] = records["abstract"].apply(
        lambda words: [w.replace("'", "") for w in words]
    )

    records["abstract"] = records["abstract"].apply(lambda words: [w for w in words if len(w) > 2])

    return records


def extract_sentences(records):
    """
    :meta private:
    """
    abstracts = records[["article", "title", "abstract"]].dropna()
    abstracts["abstract"] = abstracts["abstract"].apply(
        lambda paragraph: TextBlob(paragraph).sentences
    )
    abstracts = abstracts.explode("abstract")
    abstracts["phrase"] = abstracts["abstract"]
    abstracts["abstract"] = abstracts["abstract"].apply(lambda sentence: sentence.words)

    return abstracts
