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
>>> directory = "data/regtech/"

>>> stemming_and(
...     "author_keywords", 
...     "launder money",
...     directory=directory,
... ).head(10)
0                           anti-money laundering
1                           anti money laundering
2    banking money laundering terrorist financing
3                                money laundering
Name: author_keywords, dtype: object

>>> stemming_or(
...     "author_keywords",
...     "launder money",
...     directory=directory,
... ).head(10)
0                           anti-money laundering
1                           anti money laundering
2    banking money laundering terrorist financing
3                                money laundering
4           legalization (laundering) of proceeds
Name: author_keywords, dtype: object

"""
import string

from nltk.stem import PorterStemmer, SnowballStemmer

from ._read_records import read_records


def stemming_and(
    column,
    pattern,
    directory="./",
    stemmer="porter",
    sep=";",
    database="documents",
):
    return _stemming(
        directory=directory,
        column=column,
        pattern=pattern,
        stemmer=stemmer,
        sep=sep,
        operator="AND",
        database=database,
    )


def stemming_or(
    column,
    pattern,
    directory="./",
    stemmer="porter",
    sep=";",
    database="documents",
):
    return _stemming(
        directory=directory,
        column=column,
        pattern=pattern,
        stemmer=stemmer,
        sep=sep,
        operator="OR",
        database=database,
    )


def _stemming(
    column,
    pattern,
    stemmer,
    operator,
    directory,
    database,
    sep,
):

    if stemmer == "porter":
        stemmer = PorterStemmer()
    elif stemmer == "snowball":
        stemmer = SnowballStemmer("english")
    else:
        raise ValueError(f"Stemmer {stemmer} not supported")

    # explodes the column
    documents = read_records(
        directory=directory,
        database=database,
        use_filter=False,
    )
    documents = documents[[column]]
    documents = documents.dropna()
    documents[column] = documents[column].str.split(sep)
    documents = documents.explode(column)
    documents[column] = documents[column].str.strip()

    # stemming
    documents = documents.assign(words=documents[column])
    documents["words"] = documents["words"].str.replace("_", " ")
    documents["words"] = documents["words"].str.replace("-", " ")
    documents["words"] = documents["words"].str.replace(
        "[" + string.punctuation + "]", "", regex=True
    )
    documents["words"] = documents["words"].str.split()
    documents["words"] = documents["words"].map(
        lambda x: set(stemmer.stem(word) for word in x)
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

    result = result.drop_duplicates()
    result = result.reset_index(drop=True)

    return result
