"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetCompareFieldMixin:
    """:meta private:"""

    def set_compare_field(self, field):
        """:meta private:"""

        self.compare_field = field
        return self
