"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetSourceFieldMixin:
    """:meta private:"""

    def set_source_field(self, field):
        """:meta private:"""

        self.source_field = field
        return self
