# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pandas as pd


def nx_node_degrees_to_dataframe(node_degrees):
    """Converts a list of degrees to a dataframe."""

    dataframe = pd.DataFrame(node_degrees, columns=["Name", "Degree"])
    dataframe["Node"] = dataframe.index
    dataframe = dataframe[["Node", "Name", "Degree"]]

    return dataframe