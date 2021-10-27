import pandas as pd
from techminer.utils.datastore import load_datastore


class Coverage:
    """
    Coverage

    """

    def __init__(
        self,
        datastorepath="./",
    ):
        self._datastorepath = datastorepath
        self._datastore = load_datastore(self._datastorepath)
        self._table = None

    def _compute_coverage(self):
        """
        Compute coverage

        """
        x = self._datastore.copy()
        columns = sorted(x.columns)

        self._table = pd.DataFrame(
            {
                "Column": columns,
                "Number of items": [len(x) - x[col].isnull().sum() for col in columns],
                "Coverage (%)": [
                    "{:5.2%}".format((len(x) - x[col].isnull().sum()) / len(x))
                    for col in columns
                ],
            }
        )

    @property
    def table_(self):
        """
        Coverage table.

        """
        if self._table is None:
            self._compute_coverage()
        return self._table
