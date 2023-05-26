"""
Summary view --- ChatGPT
===============================================================================

This function returns a dataframe with the coverage (percentage of no nulls) 
and the number of different terms (topics) of each column in the dataset.

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.summary_view(root_dir).head()
           column  number of terms coverage (%)
0        abstract               48       92.31%
1  abstract_words               47       90.38%
2    affiliations               52      100.00%
3          art_no                8       15.38%
4         article               52      100.00%

"""
import pandas as pd

from ..record_utils import read_records


def summary_view(
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """
    Returns an coverage report of the dataset.

    Parameters
    ----------
    root_dir: str
        path to the root directory of the project.

    Returns
    -------
    pandas.DataFrame
        Coverage statistcs
    """
    documents = read_records(
        root_dir=root_dir,
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
