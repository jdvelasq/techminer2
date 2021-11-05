"""
Terms per year analysis
===============================================================================
"""
import numpy as np
import pandas as pd

from .utils import adds_counters_to_axis, explode, load_filtered_documents


def terms_per_year_analysis(
    directory,
    column,
    metric="num_documents",
    sep="; ",
):
    documents = load_filtered_documents(directory)
    documents = documents.assign(num_documents=1)
    exploded = explode(
        documents[
            [
                "pub_year",
                column,
                "num_documents",
                "local_citations",
                "global_citations",
                "document_id",
            ]
        ],
        column,
        sep,
    )
    table = exploded.groupby([column, "pub_year"], as_index=False).agg(
        {
            "num_documents": np.sum,
            "local_citations": np.sum,
            "global_citations": np.sum,
        }
    )

    table = table[["pub_year", column, metric]].copy()

    table = table.pivot(
        values=metric,
        index="pub_year",
        columns=column,
    )

    table = table.fillna(0)

    table = adds_counters_to_axis(
        documents, table, axis="columns", column=column, sep="; "
    )

    table = adds_counters_to_axis(
        documents, table, axis="index", column="pub_year", sep=None
    )

    table = table.sort_index(level=1, axis="columns", ascending=False)
    table = table.astype(int)

    return table

    # ##
    # ##  Number of documents and times cited by term per year
    # ##

    # result = x.groupby([self.column, "Year"], as_index=False).agg(
    #     {"Global_Citations": np.sum, "Num_Documents": np.size}
    # )
    # result = result.assign(
    #     ID=x.groupby([self.column, "Year"]).agg({"ID": list}).reset_index()["ID"]
    # )
    # result["Global_Citations"] = result["Global_Citations"].map(lambda x: int(x))

    # ##
    # ##  Summary per year
    # ##
    # summ = explode(x[["Year", "Global_Citations", "ID"]], "Year")
    # summ.loc[:, "Num_Documents"] = 1
    # summ = summ.groupby("Year", as_index=True).agg(
    #     {"Global_Citations": np.sum, "Num_Documents": np.size}
    # )

    # ##
    # ##  Dictionaries using the year as a key
    # ##
    # num_documents_by_year = {
    #     key: value for key, value in zip(summ.index, summ.Num_Documents)
    # }
    # global_citations_by_year = {
    #     key: value for key, value in zip(summ.index, summ.Global_Citations)
    # }

    # ##
    # ##  Indicators from ScientoPy
    # ##
    # result["summary_documents_by_year"] = result.Year.apply(
    #     lambda w: num_documents_by_year[w]
    # )
    # result["summary_documents_by_year"] = result.summary_documents_by_year.map(
    #     lambda w: 1 if w == 0 else w
    # )
    # result["summary_global_citations_by_year"] = result.Year.apply(
    #     lambda w: global_citations_by_year[w]
    # )
    # result[
    #     "summary_global_citations_by_year"
    # ] = result.summary_global_citations_by_year.map(lambda w: 1 if w == 0 else w)

    # result["Perc_Num_Documents"] = 0.0
    # result = result.assign(
    #     Perc_Num_Documents=round(
    #         result.Num_Documents / result.summary_documents_by_year * 100, 2
    #     )
    # )

    # result["Perc_Global_Citations"] = 0.0
    # result = result.assign(
    #     Perc_Global_Citations=round(
    #         result.Global_Citations / result.summary_global_citations_by_year * 100,
    #         2,
    #     )
    # )

    # result.pop("summary_documents_by_year")
    # result.pop("summary_global_citations_by_year")

    # result = result.rename(
    #     columns={
    #         "Num_Documents": "Num_Documents_per_Year",
    #         "Global_Citations": "Global_Citations_per_Year",
    #         "Perc_Num_Documents": "%_Num_Documents_per_Year",
    #         "Perc_Global_Citations": "%_Global_Citations_per_Year",
    #     }
    # )

    # ## Limit to
    # limit_to = self.limit_to
    # if isinstance(limit_to, dict):
    #     if self.column in limit_to.keys():
    #         limit_to = limit_to[self.column]
    #     else:
    #         limit_to = None

    # if limit_to is not None:
    #     result = result[result[self.column].map(lambda w: w in limit_to)]

    # ## Exclude
    # exclude = self.exclude
    # if isinstance(exclude, dict):
    #     if self.column in exclude.keys():
    #         exclude = exclude[self.column]
    #     else:
    #         exclude = None

    # if exclude is not None:
    #     result = result[result[self.column].map(lambda w: w not in exclude)]

    # return result


# def _terms_per_year_from_dirpath(
#     dirpath,
#     column,
#     metric,
#     sep,
# ):
#     return _terms_per_year_from_records(
#         documents=load_filtered_documents(dirpath),
#         column=column,
#         metric=metric,
#         sep=sep,
#     )


# def terms_per_year_table(
#     dirpath_or_records,
#     column,
#     metric="n_records",
#     sep="; ",
# ):
#     """
#     Counts the number of terms by record.

#     :param dirpath_or_records: path to the directory or the records object
#     :param column: column to be used to count the terms
#     :param sep: separator to be used to split the column
#     :return: a pandas.Series with the number of terms by record.
#     """

#     if isinstance(dirpath_or_records, str):
#         return _terms_per_year_from_dirpath(
#             dirpath=dirpath_or_records,
#             column=column,
#             metric=metric,
#             sep=sep,
#         )
#     elif isinstance(dirpath_or_records, pd.DataFrame):
#         return _terms_per_year_from_records(
#             documents=dirpath_or_records,
#             column=column,
#             metric=metric,
#             sep=sep,
#         )
#     else:
#         raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")
