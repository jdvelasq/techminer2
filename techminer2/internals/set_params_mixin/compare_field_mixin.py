"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class CompareFieldMixin:
    """:meta private:"""

    def compare_field(self, field):
        """:meta private:"""

        self.compare_field = field
        return self
