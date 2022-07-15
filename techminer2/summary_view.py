"""
Summary View
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> summary_view(directory).head()
           column  number of terms coverage (%)
0        abstract               89       94.68%
1  abstract_words               87       92.55%
2    affiliations               93       98.94%
3          art_no               13       13.83%
4         article               94      100.00%

"""
import pandas as pd

from ._read_records import read_records


def summary_view(directory="./", database="documents"):
    """
    Returns an coverage report of the dataset.

    Parameters
    ----------
    directory: str
        path to the directory

    Returns
    -------
    pandas.DataFrame
        Coverage statistcs
    """
    documents = read_records(directory=directory, database=database, use_filter=True)
    columns = sorted(documents.columns)
    n_documents = len(documents)
    report = pd.DataFrame(
        {
            "column": columns,
            "number of terms": [
                n_documents - documents[col].isnull().sum() for col in columns
            ],
            "coverage (%)": [
                "{:5.2%}".format(
                    (n_documents - documents[col].isnull().sum()) / n_documents
                )
                for col in columns
            ],
        }
    )

    return report
