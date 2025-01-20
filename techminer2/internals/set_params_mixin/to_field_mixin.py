"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class ToFieldMixin:
    """:meta private:"""

    def to_field(self, field):
        """:meta private:"""

        self.to_field = field
        return self
