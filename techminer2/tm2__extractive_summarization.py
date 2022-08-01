"""
Abstracts Extractive Summarization
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import tm2__extractive_summarization
>>> tm2__extractive_summarization(
...     criterion="author_keywords",
...     custom_topics=["blockchain"],
...     n_abstracts=20,    
...     n_phrases_per_algorithm=20,
...     directory=directory,
... )
extractive_summarization.txt
authors of this paper investigate how blockchain can be used to secure stock exchange
transactions, with an especial focus to the technological as well as legal aspects of such
applications. >> blockchain (bc) technology, being distributed and immutable in nature,
has proved to the 'trust machine' eliminating the need for third-parties. >> however, to
create valid legal effects blockchains should be anchored prudently in the surrounding
legal context and specific regulations will be supportive to unfold their potential in a
sustainable way and in an international context. >> in this work, we propose a blockchain-
based regtech system which helps to track the credit of organizations. >> pace of
transition can be seen in particular in the position of emerging technology, also
summarized as the abcd framework: artificial intelligence ("ai"), blockchain, cloud and
technology, which are rapidly co-evolving with finance. >> though blockchain technology
has been leveraged to increase effectiveness of certain corporate banking products, the
originality of the paper lies in coming out with a detailed framework for the possible use
of blockchain (a distributed ledger based technology) for credit decisions, timely
generation of red-flags and tightening the regulatory framework.
<BLANKLINE>


"""
import os
import textwrap

from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

from ._read_records import read_records


def tm2__extractive_summarization(
    criterion,
    custom_topics,
    file_name="extractive_summarization.txt",
    n_abstracts=50,
    n_phrases_per_algorithm=5,
    quiet=False,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Abstract extractive summarization using sumy."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = _select_records(criterion, custom_topics, n_abstracts, records)
    document = _create_document(records)
    summary_with_lexrank = _summarize_with_lexrank(document, n_phrases_per_algorithm)
    summary_with_lsasummarizer = _summarize_with_lsasummarizer(
        document, n_phrases_per_algorithm
    )
    summary_with_luhn = _summarize_with_luhn(document, n_phrases_per_algorithm)
    summary_with_klsummarizer = _summarize_with_klsummarizer(
        document, n_phrases_per_algorithm
    )

    summary = (
        summary_with_lexrank
        + summary_with_lsasummarizer
        + summary_with_luhn
        + summary_with_klsummarizer
    )
    summary = list(set(summary))

    final_summary = []
    for topic in custom_topics:
        for sentence in summary:
            if topic in sentence:
                final_summary.append(sentence)

    final_summary = sorted(set(final_summary))

    final_summary = " >> ".join(final_summary)
    final_summary = textwrap.fill(final_summary, width=90)

    with open(
        os.path.join(directory, "reports", file_name), "w", encoding="utf-8"
    ) as out_file:

        print(final_summary, file=out_file)

    if quiet is False:
        print(file_name)
        print(final_summary)
        print()


def _summarize_with_klsummarizer(document, n_phrases_per_algorithm):
    parser = PlaintextParser.from_string(document, Tokenizer("english"))
    summarizer = KLSummarizer()
    summary = summarizer(parser.document, n_phrases_per_algorithm)
    summary = [str(sentence) for sentence in summary]
    return summary


def _summarize_with_luhn(document, n_phrases_per_algorithm):
    parser = PlaintextParser.from_string(document, Tokenizer("english"))
    summarizer = LuhnSummarizer()
    summary = summarizer(parser.document, n_phrases_per_algorithm)
    summary = [str(sentence) for sentence in summary]
    return summary


def _summarize_with_lsasummarizer(document, n_phrases_per_algorithm):
    parser = PlaintextParser.from_string(document, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, n_phrases_per_algorithm)
    summary = [str(sentence) for sentence in summary]
    return summary


def _summarize_with_lexrank(document, n_phrases_per_algorithm):
    parser = PlaintextParser.from_string(document, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, n_phrases_per_algorithm)
    summary = [str(sentence) for sentence in summary]
    return summary


def _create_document(records):
    abstracts = records["abstract"]
    abstracts = abstracts.dropna()
    document = "\n".join(abstracts.tolist())
    return document


def _select_records(criterion, custom_topics, n_abstracts, records):
    selected_records = records[["article", criterion]]
    selected_records[criterion] = selected_records[criterion].str.split(";")
    selected_records = selected_records.explode(criterion)
    selected_records[criterion] = selected_records[criterion].str.strip()
    selected_records = selected_records[selected_records[criterion].isin(custom_topics)]
    records = records[records["article"].isin(selected_records["article"])]

    records = records.sort_values(
        by=["global_citations", "local_citations"], ascending=False
    )
    records = records.head(n_abstracts)
    return records
