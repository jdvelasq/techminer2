"""
Abstract Summarization
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import tlab__abstract_summarization
>>> tlab__abstract_summarization(
...     texts=["fintech", "blockchain"],
...     n_phrases=5,    
...     directory=directory,
... )
Featuring coverage on a broad range of topics such as crowdfunding platforms, crypto-
assets, and BLOCKCHAIN technology, this book is ideally designed for researchers,
economists, practitioners, policymakers, analysts, managers, executives, educators, and
students seeking current research on the strategic role of technology in the future
development of financial and economic activity. >>> Since the market events took place in
electronic markets, and algorithmic trading and high-frequency trading, parts of FINTECH,
played significant roles, we handle the may 6 flash crash from the FINTECH, suptech, and
financial supervision perspectives. >>> This new regulatory model aims to build a system
that integrates equal access to information on BLOCKCHAIN transactions by both parties to
it (i.e., the regulators and the financial institutions they regulate) for the purpose of
oversight, intelligent real-time oversight, and an experimental sandbox for developing
regulatory technology. >>> Pace of transition can be seen in particular in the position of
emerging technology, also summarized as the abcd framework: artificial intelligence
("ai"), BLOCKCHAIN, cloud and technology, which are rapidly co-evolving with finance. >>>
The development of financial technology ('FINTECH'), rapid developments in emerging
markets, and the recent pro-active stance of regulators in developing regulatory
sandboxes, represent a unique combination of events, which could facilitate the transition
from one regulatory model to another.

"""
import os
import textwrap

import nltk
from nltk.stem import PorterStemmer

from ._load_abstracts import load_abstracts
from ._read_records import read_records


def tlab__abstract_summarization(
    texts=None,
    n_phrases=10,
    sufix="",
    directory="./",
):

    if isinstance(texts, str):
        texts = [texts]

    abstracts = load_abstracts(directory)
    documents = read_records(directory)

    regex = r"\b(" + "|".join(texts) + r")\b"

    abstracts = abstracts[abstracts.phrase.str.contains(regex, regex=True)]
    abstracts = abstracts[["article", "phrase"]]

    # -----------------------------------------------------------------------------------
    porter_stemmer = PorterStemmer()

    abstracts["formatted_text"] = abstracts.phrase.copy()
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(
        r"[[0-9]]*", " "
    )
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(r"s+", " ")
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(
        r"[a-zA-Z]", " "
    )
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(r"s+", " ")
    #
    stopwords = nltk.corpus.stopwords.words("english")
    word_frequencies = {}
    for phrase in abstracts["formatted_text"].values:
        for word in nltk.word_tokenize(phrase):
            word = porter_stemmer.stem(word)
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
    #
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequncy

    #

    abstracts["sentence_scores"] = 0
    for index, row in abstracts.iterrows():
        for word in nltk.word_tokenize(row["formatted_text"]):
            word = porter_stemmer.stem(word)
            if word in word_frequencies.keys():
                abstracts.at[index, "sentence_scores"] += word_frequencies[word]

        # length = len(nltk.word_tokenize(row["formatted_text"]))
        # abstracts.at[index, "sentence_scores"] /= max(1, length)

    abstracts = abstracts.sort_values(by=["sentence_scores"], ascending=False)

    abstracts = abstracts.head(n_phrases)
    abstracts["phrase"] = abstracts.phrase.str.capitalize()

    for text in texts:
        abstracts["phrase"] = abstracts["phrase"].str.replace(text, text.upper())
        abstracts["phrase"] = abstracts["phrase"].str.replace(
            text.capitalize(), text.upper()
        )

    with open(
        os.path.join(directory, "reports", f"abstract_summarization{sufix}.txt"), "w"
    ) as out_file:
        for index, row in abstracts.iterrows():
            paragraph = textwrap.fill(
                row["phrase"],
                width=90,
            )
            article = documents[documents.article == row["article"]].article
            article = article.iloc[0]
            print("*** " + article, file=out_file)
            print(paragraph, file=out_file)
            print("\n", file=out_file)

    summary = " >>> ".join(abstracts.phrase.values)

    print(textwrap.fill(summary, width=90))

    # return abstracts
