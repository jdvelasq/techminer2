# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines item param filters."""


class ColumnsAndRowsParamsMixin:
    """:meta private:"""

    def set_columns_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.columns_params, key):
                setattr(self.columns_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ColumnsParams: {key}")
        return self

    def set_rows_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.rows_params, key):
                setattr(self.rows_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for RowsParams: {key}")
        return self
