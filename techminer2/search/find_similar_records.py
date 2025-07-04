# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Find Similar Records
===============================================================================


## >>> from techminer2.search import find_similar_records
## >>> documents = find_similar_records(
## ...     #
## ...     # SEARCH PARAMS:
## ...     record_no=1,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/",
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> for i in range(2):
## ...    print(documents[i])
SIMILARITY: 1.0
Record-No: 1
AR Goldstein I., 2019, REV FINANC STUD, V32, P1647
TI To FinTech and beyond
AU Goldstein I.; Jiang W./1; Karolyi G.A.
TC 197
SO Review of Financial Studies
PY 2019
AB FINTECH is about the introduction of NEW_TECHNOLOGIES into the
   FINANCIAL_SECTOR , and IT is now revolutionizing the FINANCIAL_INDUSTRY . in
   2017 , when the academic FINANCE COMMUNITY was not actively researching
   FINTECH , the EDITORIAL_TEAM of the REVIEW of FINANCIAL_STUDIES launched a
   COMPETITION to develop RESEARCH_PROPOSALS focused on this topic . this
   SPECIAL_ISSUE is the result . in this INTRODUCTORY_ARTICLE , we describe the
   RECENT_FINTECH_PHENOMENON and the NOVEL_EDITORIAL_PROTOCOL employed for this
   SPECIAL_ISSUE following the registered reports format.we discuss what we
   learned from the submitted proposals about the field of FINTECH and which
   ones we selected to be completed and ultimately come out in this
   SPECIAL_ISSUE . we also provide several observations to help guide
   FUTURE_RESEARCH in the emerging area of FINTECH . ( JEL_G00 , G21 , g23 ,
   G28 , l51 , o31 ) . the author ( s ) 2019 .
** EDITORIAL_TEAM; FINANCIAL_INDUSTRY; FINANCIAL_SECTOR; FINANCIAL_STUDIES;
   FUTURE_RESEARCH; INTRODUCTORY_ARTICLE; JEL_G00; NEW_TECHNOLOGIES;
   NOVEL_EDITORIAL_PROTOCOL; RECENT_FINTECH_PHENOMENON; RESEARCH_PROPOSALS;
   SPECIAL_ISSUE
<BLANKLINE>
SIMILARITY: 0.217
Record-No: 32
AR Zavolokina L., 2016, INT CONF INF SYST ICIS
TI FinTech - What's in a name?
AU Zavolokina L.; Dolata M.; Schwabe G.
TC 75
SO 2016 International Conference on Information Systems, ICIS 2016
PY 2016
AB FINTECH , the word which originates from marriage of " FINANCE " and "
   TECHNOLOGY " , designates currently a novel , innovative and emerging field
   which ATTRACTS_ATTENTION from the publicity . at the moment there is no
   UNIVERSAL_UNDERSTANDING and DEFINITION of FINTECH in the RESEARCH , however
   , the topic is widely addressed by the english_ and german_speaking press .
   in this study we aim to make insights into how the press and other
   POPULAR_MEDIA understand and FRAME_FINTECH , discussing definitions that
   represents the meaning of IT for the press , and deliver the
   CONCEPTUAL_FRAMEWORK to be used in RESEARCH and SCIENTIFIC_LITERATURE . in
   doing so , we also IDENTIFY_DRIVERS of FINTECH and put them in the CONTEXT
   of financial and DIGITAL_INNOVATION_RESEARCH . thereby , we provide
   OBJECTIVE_UNDERSTANDING of FINTECH , how IT is reflected in the
   POPULAR_MEDIA .
DE CONTENT_ANALYSIS; DIGITALIZATION; FINTECH; INNOVATION; POPULAR_PRESS
ID INFORMATION_SYSTEMS; INNOVATION; CONCEPTUAL_FRAMEWORKS; CONTENT_ANALYSIS;
   DIGITAL_INNOVATIONS; DIGITALIZATION; FINTECH; SCIENTIFIC_LITERATURE; PRESSES
   (MACHINE_TOOLS)
** ATTRACTS_ATTENTION; CONCEPTUAL_FRAMEWORK; DIGITAL_INNOVATION_RESEARCH;
   FINTECH; FRAME_FINTECH; IDENTIFY_DRIVERS; OBJECTIVE_UNDERSTANDING;
   POPULAR_MEDIA; SCIENTIFIC_LITERATURE; UNIVERSAL_UNDERSTANDING
<BLANKLINE>


"""
from nltk.stem import WordNetLemmatizer  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore
from textblob import TextBlob  # type: ignore

# from ..database.load.load__database import load__filtered_database
# from ..database.tools.record_viewer import select_documents

TEXTWRAP_WIDTH = 73


def find_similar_records(
    #
    # SEARCH PARAMS:
    record_no,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """:meta private:"""

    #
    # Load the abstracts
    records = load__filtered_database(
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
        **filters,
    )
    records = records.dropna(subset=["abstract"])

    #
    #
    records["paragraph"] = records["abstract"].copy()
    records["paragraph"] = records["paragraph"].str.lower()

    records = records.loc[records.paragraph != "[no abstract available]", :]

    records["paragraph"] = records["paragraph"].str.replace("_", " ")

    #
    #
    records = _paragraph_to_meaningful_words(records)
    tf_matrix = _build_tf_matrix(records)
    similarity = cosine_similarity(tf_matrix, [tf_matrix.loc[record_no, :].values])
    records["similarity"] = similarity
    records = records.sort_values(by="similarity", ascending=False)
    records = records[records["similarity"] > 0.0]

    documents = select_documents(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **{"record_id": records.record_id.tolist()},
        **filters,
    )

    sorted_documents = []
    for _, record in records.iterrows():
        doc = [doc for doc in documents if record.record_id in doc]
        assert len(doc) == 1
        doc = "SIMILARITY: " + str(round(record.similarity, 3)) + "\n" + doc[0]
        sorted_documents.append(doc)

    return sorted_documents


def _paragraph_to_meaningful_words(records):

    lemmatizer = WordNetLemmatizer()

    def to_lemma(tag):
        if tag[1][:2] == "NN":
            return (lemmatizer.lemmatize(tag[0], pos="n"), tag[1])

        if tag[1][:2] == "VB":
            return (lemmatizer.lemmatize(tag[0], pos="v"), tag[1])

        if tag[1][:2] == "RB":
            return (lemmatizer.lemmatize(tag[0], pos="r"), tag[1])

        if tag[1][:2] == "JJ":
            return (lemmatizer.lemmatize(tag[0], pos="a"), tag[1])

        return lemmatizer.lemmatize(tag[0]), tag[1]

    records = records.copy()
    records = records[
        ["art_no", "record_id", "document_title", "abstract", "paragraph"]
    ].dropna()

    #
    # Split the  abstract in sentences
    records["paragraph"] = records["paragraph"].apply(
        lambda paragraph: TextBlob(paragraph).sentences
    )

    #
    # Extracts the meaningful words from each sentence
    records["paragraph"] = records["paragraph"].apply(
        lambda sentences: [sentence.tags for sentence in sentences]
    )

    records["paragraph"] = records["paragraph"].apply(
        lambda sentences: [
            tag
            for sentence in sentences
            for tag in sentence
            if tag[1][:2] in ["NN", "VB", "RB", "JJ"]
        ]
    )

    records["paragraph"] = records["paragraph"].apply(
        lambda tags: [to_lemma(tag) for tag in tags]
    )

    records["paragraph"] = records["paragraph"].apply(
        lambda tags: [tag[0] for tag in tags]
    )

    records["paragraph"] = records["paragraph"].apply(set)
    records["paragraph"] = records["paragraph"].apply(sorted)

    return records


def _build_tf_matrix(records):

    records = records.copy()
    records = records.explode("paragraph")
    records["OCC"] = 1
    records = records.pivot(index="art_no", columns="paragraph", values="OCC")
    records = records.fillna(0)
    return records
