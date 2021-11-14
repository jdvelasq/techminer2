"""
Column indicators by year
===============================================================================



"""
from .utils import load_filtered_documents


def column_indicators_by_year(directory=None, column="authors", sep="; "):
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
    report = report.reset_index(drop=True)

    return report
