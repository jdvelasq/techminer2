"""
Colaboration Analysis
===============================================================================

"""


import numpy as np
import pandas as pd

from .utils import explode, load_records_from_directory


def _collaboration_analysis_from_records(
    records,
    column,
    sep,
):

    records = records.copy()
    records["SD"] = records[column].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0
    )
    records["MD"] = records[column].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0
    )

    x = explode(
        records[
            [
                column,
                "SD",
                "MD",
                "record_id",
            ]
        ],
        column=column,
        sep=sep,
    )
    result = x.groupby(column, as_index=False).agg(
        {
            "SD": np.sum,
            "MD": np.sum,
        }
    )
    result["SMR"] = [round(MD / max(SD, 1), 2) for SD, MD in zip(result.SD, result.MD)]
    result = result.set_index(column)

    ## limit to / exclude options
    # result = exclude_terms(data=result, axis=0)

    ## counters in axis names
    # result = add_counters_to_axis(
    #     X=result, axis=0, data=self.data, column=self.column
    # )

    ## Top by / Top N
    # result = sort_by_axis(data=result, sort_by=self.top_by, ascending=False, axis=0)
    # result = result.head(self.max_items)

    ## Sort by
    # if self.sort_by in result.columns:
    #     result = result.sort_values(self.sort_by, ascending=self.ascending)
    # else:
    #     result = sort_by_axis(
    #         data=result, sort_by=self.sort_by, ascending=self.ascending, axis=0
    #     )

    # if self.view == "Table":
    #     return result

    # if self.view == "Bar plot":
    #     return stacked_bar(
    #         X=result[["SD", "MD"]],
    #         cmap=self.colormap,
    #         ylabel="Num Documents",
    #         figsize=(self.width, self.height),
    #     )

    # if self.view == "Horizontal bar plot":
    #     return stacked_barh(
    #         X=result[["SD", "MD"]],
    #         cmap=self.colormap,
    #         xlabel="Num Documents",
    #         figsize=(self.width, self.height),
    #     )

    return result


def _collaboration_analysis_from_directory(
    directory,
    column,
    sep,
):
    return _collaboration_analysis_from_records(
        records=load_records(directory),
        column=column,
        sep=sep,
    )


def collaboration_analysis(
    directory_or_records,
    column,
    sep="; ",
):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    directory_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """
    if isinstance(directory_or_records, str):
        return _collaboration_analysis_from_directory(
            directory=directory_or_records,
            column=column,
            sep=sep,
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _collaboration_analysis_from_records(
            records=directory_or_records,
            column=column,
            sep=sep,
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
