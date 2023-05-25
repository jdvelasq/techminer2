"""
Define classes for retorning the results of the functions.
"""

from dataclasses import dataclass

import pandas as pd


@dataclass(init=False)
class NetworkStatistics:
    """Network statistics."""

    table_: pd.DataFrame
    prompt_: str
