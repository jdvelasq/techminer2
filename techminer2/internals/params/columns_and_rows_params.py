# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines item param filters."""


class ColumnsAndRowsParamsMixin:
    """:meta private:"""

    def set_columns_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.column_params, key):
                setattr(self.column_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ColumnParams: {key}")
        return self

    def set_rows_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.row_params, key):
                setattr(self.row_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for RowParams: {key}")
        return self
