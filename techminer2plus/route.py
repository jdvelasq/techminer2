# flake8: noqa
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
"""
Route
==============================================================================




"""
from dataclasses import dataclass


@dataclass
class Route:
    """Records"""

    #
    # PARAMS:
    #
    root_dir: str = "./"

    #
    #
    def summary_sheet(self):
        """
        Summary sheet

        >>> import techminer2plus as tm
        >>> root_dir = "data/regtech/"
        >>> tm.Route(root_dir).summary_sheet()
        'hola'




        """

        return "hola"
