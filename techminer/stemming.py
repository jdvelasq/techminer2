"""
Stemming  AND & OR operators 
===============================================================================

Searchs in the terms of a column using stemming

**Algorithm**:

    1. Takes a single item in the column
    2. breaks the item in individual words
    3. stems each word
    4. searches the list for matches of the stems using AND or OR operator.




>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> stemming_and(directory, "author_keywords", "intelligence business").head(10)
2022-0001           business intelligence
2020-0361    business intelligence and ai
2020-0065           business intelligence
2019-0163           business intelligence
Name: author_keywords, dtype: object

>>> stemming_or(directory, "author_keywords", "intelligence business").head(10)
record_no
2022-0001                      business intelligence
2022-0004                    artificial intelligence
2022-0005                    artificial intelligence
2022-0006                 intelligent transportation
2021-0247                    artificial intelligence
2021-0109               artificial intelligence (ai)
2021-0109                        intelligent systems
2021-0257                         e-business systems
2021-0090    artificial intelligence (ai) governance
2021-0322                    artificial intelligence
Name: author_keywords, dtype: object

"""
import string

import pandas as pd
from nltk.stem import PorterStemmer, SnowballStemmer

from .utils import load_filtered_documents


def _stemming(directory, column, pattern, stemmer="porter", sep="; ", operator="AND"):

    if stemmer == "porter":
        stemmer = PorterStemmer()
    elif stemmer == "snowball":
        stemmer = SnowballStemmer("english")
    else:
        raise ValueError(f"Stemmer {stemmer} not supported")

    # explodes the column
    documents = load_filtered_documents(directory)
    documents = documents[[column]]
    documents = documents.dropna()
    documents[column] = documents[column].str.split(sep)
    documents = documents.explode(column)

    # stemming
    documents = documents.assign(words=documents[column])
    documents["words"] = documents["words"].str.replace("_", " ")
    documents["words"] = documents["words"].str.replace("-", " ")
    documents["words"] = documents["words"].str.replace(
        "[" + string.punctuation + "]", "", regex=True
    )
    documents["words"] = documents["words"].str.split()
    documents["words"] = documents["words"].map(
        lambda x: set([stemmer.stem(word) for word in x])
    )

    # patter preparation
    pattern = pattern.replace("_", " ")
    pattern = pattern.replace("-", " ")
    pattern = pattern.translate(pattern.maketrans("", "", string.punctuation))

    pattern = pattern.split()
    pattern = set([stemmer.stem(word) for word in pattern])

    # operator
    if operator == "AND":
        documents["words"] = documents["words"].map(lambda x: pattern.difference(x))
        documents["words"] = documents["words"].map(len)
        documents = documents.query("words == 0")
        result = documents[column].copy()
    elif operator == "OR":
        documents["words"] = documents["words"].map(lambda x: pattern.intersection(x))
        documents["words"] = documents["words"].map(len)
        documents = documents.query("words > 0")
        result = documents[column].copy()
    else:
        raise ValueError(f"Operator {operator} not supported")

    return result


def stemming_and(directory, column, pattern, stemmer="porter", sep="; "):
    return _stemming(
        directory=directory,
        column=column,
        pattern=pattern,
        stemmer=stemmer,
        sep=sep,
        operator="AND",
    )


def stemming_or(directory, column, pattern, stemmer="porter", sep="; "):
    return _stemming(
        directory=directory,
        column=column,
        pattern=pattern,
        stemmer=stemmer,
        sep=sep,
        operator="OR",
    )
