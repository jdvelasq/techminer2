# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pandas as pd


def internal__create_node_degrees_data_frame(node_degrees):
    """Converts a list of degrees to a dataframe."""

    dataframe = pd.DataFrame(node_degrees, columns=["Name", "Degree"])
    dataframe["counters"] = dataframe.Name.map(lambda x: x.split(" ")[-1])
    dataframe = dataframe.sort_values(
        by=["Degree", "counters", "Name"], ascending=[False, False, True]
    )
    dataframe = dataframe.reset_index(drop=True)
    dataframe["Node"] = dataframe.index
    dataframe = dataframe[["Node", "Name", "Degree"]]

    return dataframe
