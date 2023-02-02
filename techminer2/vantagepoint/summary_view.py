"""
Summary View
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.summary_view(directory).head()
           column  number of terms coverage (%)
0        abstract               48       92.31%
1  abstract_words               47       90.38%
2    affiliations               52      100.00%
3          art_no                8       15.38%
4         article               52      100.00%

"""
import pandas as pd

from .._lib._read_records import read_records


def summary_view(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
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
    documents = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
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
