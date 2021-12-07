"""
Column indicators by year
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> column_indicators_by_year(directory, 'authors').head(10)
              pub_year  num_documents  global_citations  local_citations
authors                                                                 
Dolata M          2016              1                43                7
Hong S            2016              1                 2                1
Hung J-L          2016              1                24                4
Kim K             2016              1                 2                1
Kotarba M         2016              1                16                3
Luo B             2016              1                24                4
Schueffel P       2016              1               106               14
Schwabe G         2016              1                43                7
Zavolokina L      2016              1                43                7
Brooks S          2017              1               146               15

"""
from .utils import load_filtered_documents


def column_indicators_by_year(directory=None, column="authors"):
    """
    Counts the number of terms by record per year.

    :param dirpath_or_records: path to the directory or the records object
    :param column: column to be used to count the terms
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of terms by record.
    """

    report = load_filtered_documents(directory)
    report = report.assign(num_documents=1)
    report = report[
        [column, "num_documents", "global_citations", "local_citations", "pub_year"]
    ].copy()

    if sep is not None:
        report[column] = report[column].str.split(sep)
        report = report.explode(column)

    report = (
        report.groupby([column, "pub_year"], as_index=False)
        .sum()
        .sort_values(by=["pub_year", column], ascending=True)
    )
    report["num_documents"] = report.num_documents.astype(int)
    report["global_citations"] = report.global_citations.astype(int)
    report["local_citations"] = report.local_citations.astype(int)
    report = report.dropna()
    report = report.set_index(column)

    return report
