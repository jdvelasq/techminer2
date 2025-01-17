"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetToFieldMixin:
    """:meta private:"""

    def set_to_field(self, field):
        """:meta private:"""

        self.to_field = field
        return self
