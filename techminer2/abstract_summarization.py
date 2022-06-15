"""
Abstract Summarization
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> abstract_summarization(
...     texts=["fintech", "blockchain"],
...     n_phrases=5,    
...     directory=directory,
... )
The research on data science and ai in FINTECH involves many latest progress made in smart
FINTECH for bankingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
cryptocurrencies, and BLOCKCHAIN, and the dsai techniques including complex system
methods, quantitative methods, intelligent interactions, recognition and responses, data
analytics, deep learning, federated learning, privacy-preserving processing, augmentation,
optimization, and system intelligence enhancement... From the theoretical point of view,
our research indicates, that besides key growth driving factors, outlined in existing
literature, such as strategy, prerequisites for rapid growth, business model choice,
international business networks, entrepreneur's characteristics, product development or
theoretical frameworks for development, especially within the international market, the
quality of digital logistics performance of FINTECH companies seem to matter... Internet
banking, mobile banking, atm,cash deposit machines, instant payment services, online
trading in stock markets, online funds transfers, e-wallets,wealth management, peer to
peer lending, BLOCKCHAIN technology are various FINTECH products and services... The most
important factors that influence the level of satisfaction when using FINTECH services
were considered: comfort and ease of use, legal regulations, ease of account opening,
mobile payments features, crowdfunding options, international money transfers features,
reduced costs associated with transactions, peer-to-peer lending, insurances options,
online brokerage, cryptocoins options and exchange options... Fourth, the traditional
assets, gold and oil, as well as modern assets, green bonds, are useful as good hedgers
compared with other assets because shock transmissions from them to FINTECH, kftx are
below 0.1% and, more importantly, the total volatility spill-over of all assets in the
sample is moderately average, accounting for 44.39%.




"""


import os
import textwrap

import nltk
import pandas as pd
from nltk.stem import PorterStemmer

from .load_abstracts import load_abstracts
from .load_filtered_documents import load_filtered_documents


def abstract_summarization(
    texts=None,
    n_phrases=10,
    sufix="",
    directory="./",
):

    if isinstance(texts, str):
        texts = [texts]

    abstracts = load_abstracts(directory)
    documents = load_filtered_documents(directory)

    regex = r"\b(" + "|".join(texts) + r")\b"

    abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
    abstracts = abstracts[["record_no", "text"]]

    # -----------------------------------------------------------------------------------
    porter_stemmer = PorterStemmer()

    abstracts["formatted_text"] = abstracts.text.copy()
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
    abstracts["text"] = abstracts.text.str.capitalize()

    for text in texts:
        abstracts["text"] = abstracts["text"].str.replace(text, text.upper())
        abstracts["text"] = abstracts["text"].str.replace(
            text.capitalize(), text.upper()
        )

    with open(
        os.path.join(directory, f"abstract_summarization{sufix}.txt"), "w"
    ) as out_file:
        for index, row in abstracts.iterrows():
            paragraph = textwrap.fill(
                row["text"],
                width=90,
            )
            document_id = documents[documents.record_no == row["record_no"]].document_id
            document_id = document_id.iloc[0]
            print("*** " + document_id, file=out_file)
            print(paragraph, file=out_file)
            print("\n", file=out_file)

    summary = ".. ".join(abstracts.text.values)

    print(textwrap.fill(summary, width=90))

    # return abstracts
