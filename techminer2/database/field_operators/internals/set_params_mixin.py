"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetParamsMixin:
    """:meta private:"""

    def set_params(self, **kwargs):
        """:meta private:"""

        for key, value in kwargs.items():
            if hasattr(self.params, key):
                setattr(self.params, key, value)
            else:
                raise ValueError(f"Invalid parameter for Params: {key}")
        return self
