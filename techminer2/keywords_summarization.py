"""
Keywords Summarization
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> keywords_summarization(
...     column="author_keywords",
...     keywords=["fintech", "block-chain"],
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

import textwrap
from os.path import isfile, join
from xml.dom import WRONG_DOCUMENT_ERR

import nltk
import pandas as pd
from nltk.stem import PorterStemmer

from .thesaurus import load_file_as_dict


def keywords_summarization(
    column,
    keywords=None,
    n_phrases=10,
    sufix="",
    directory="./",
):
    def expand_keywords(keywords):
        #
        # Expands the original keywords list to the equivalent keywords in the thesaurus.
        #
        thesaurus_file = join(directory, "keywords.txt")
        if isfile(thesaurus_file):
            th = load_file_as_dict(thesaurus_file)
        else:
            raise FileNotFoundError(
                "The file {} does not exist.".format(thesaurus_file)
            )

        # extract keys for thesaurus
        reversed_th = {value: key for key, values in th.items() for value in values}
        th_keys = []
        for keyword in keywords:
            th_keys.append(reversed_th[keyword])
        expanded_keywords = [text for key in th_keys for text in th[key]]

        return expanded_keywords

    def select_documents(documents, column, expanded_keywords):
        documents = documents.copy()
        documents.index = documents.record_no
        documents = documents[column]
        documents = documents.str.split(";")
        documents = documents.explode()
        documents = documents.str.strip()
        documents = documents.isin(expanded_keywords)
        document_id = list(set(documents.index.tolist()))
        return document_id

    def load_abstracts(documents_id, expanded_keywords):
        expanded_keywords = expanded_keywords.copy()
        file_name = join(directory, "abstracts.csv")
        abstracts = pd.read_csv(file_name)
        abstracts = abstracts[abstracts.record_no.isin(documents_id)]
        expanded_keywords = [
            word.replace("(", "\(").replace(")", "\)") for word in expanded_keywords
        ]
        regex = r"\b(" + "|".join(expanded_keywords) + r")\b"
        abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
        return abstracts

    def summarize(abstracts, expanded_keywords):

        porter_stemmer = PorterStemmer()

        abstracts = abstracts.copy()

        # Prepare text
        abstracts["formatted_text"] = abstracts.text.copy()
        replace_list = [
            (r"[[0-9]]*", " "),
            (r"s+", " "),
            (r"[a-zA-Z]", " "),
            (r"s+", " "),
        ]
        for pat, repl in replace_list:
            abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(
                pat, repl
            )

        # Count word frequency
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

        # Compute puntuation
        maximum_frequncy = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word] / maximum_frequncy

        # Scores
        abstracts["sentence_scores"] = 0
        for index, row in abstracts.iterrows():
            for word in nltk.word_tokenize(row["formatted_text"]):
                word = porter_stemmer.stem(word)
                if word in word_frequencies.keys():
                    abstracts.at[index, "sentence_scores"] += word_frequencies[word]

        # Select main phrases
        abstracts = abstracts.sort_values(by=["sentence_scores"], ascending=False)
        abstracts = abstracts.head(n_phrases)
        abstracts["text"] = abstracts.text.str.capitalize()

        for text in expanded_keywords:
            abstracts["text"] = abstracts["text"].str.replace(
                text, text.upper(), regex=False
            )
            abstracts["text"] = abstracts["text"].str.replace(
                text.capitalize(), text.upper()
            )

        return abstracts

    def save_summary(abstracts, sufix):
        with open(
            join(directory, f"abstract_summarization{sufix}.txt"), "w"
        ) as out_file:
            for _, row in abstracts.iterrows():
                paragraph = textwrap.fill(
                    row["text"],
                    width=90,
                )
                document_id = documents[
                    documents.record_no == row["record_no"]
                ].document_id
                document_id = document_id.iloc[0]
                print("*** " + document_id, file=out_file)
                print(paragraph, file=out_file)
                print("\n", file=out_file)

    # ----< data must be a list >--------------------------------------------------------
    if isinstance(keywords, str):
        keywords = [keywords]

    documents = pd.read_csv(join(directory, "documents.csv"))

    expanded_keywords = expand_keywords(keywords)
    documents_id = select_documents(documents, column, expanded_keywords)
    abstracts = load_abstracts(documents_id, expanded_keywords)
    abstracts = summarize(abstracts, expanded_keywords)

    save_summary(abstracts, sufix)

    # -----------------------------------------------------------------------------------
    summary = ".. ".join(abstracts.text.values)
    print(textwrap.fill(summary, width=90))
