"""
Stemming  AND & OR Operators 
===============================================================================

Searchs in the terms of a column using stemming

**Algorithm**:

    1. Takes a single item in the column
    2. breaks the item in individual words
    3. stems each word
    4. searches the list for matches of the stems using AND or OR operator.


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> stemming_and(directory, "author_keywords", "business model").head(10)
51             business model
107    fintech business model
111       bank business model
154            business model
202            business model
211            business model
213            business model
242            business model
Name: author_keywords, dtype: object
 
>>> stemming_or(directory, "author_keywords", "business model").head(10)
3      structural equation model (sem)
23     structural equation model (sem)
24                            modeling
48             business sustainability
48               small food businesses
51                business environment
51                      business model
58         fintech predictive modeling
66     structural equation model (sem)
107             fintech business model
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
