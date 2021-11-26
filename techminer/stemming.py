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
>>> directory = "/workspaces/techminer-api/data/"
>>> stemming_and(directory, "author_keywords", "intelligence business").head(10)
6              business intelligence
648     business intelligence and ai
1002           business intelligence
1038           business intelligence
Name: author_keywords, dtype: object

>>> stemming_or(directory, "author_keywords", "intelligence business").head(10)
6                   business intelligence
11                artificial intelligence
12                artificial intelligence
13             intelligent transportation
41                artificial intelligence
52    explainable artificial intelligence
78                artificial intelligence
96                artificial intelligence
96                    intelligent systems
98                     e-business systems
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
