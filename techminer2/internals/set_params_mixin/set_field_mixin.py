"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetFieldMixin:
    """:meta private:"""

    def set_field(self, field):
        """:meta private:"""

        self.field = field
        return self
