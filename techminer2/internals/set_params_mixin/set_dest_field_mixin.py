"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetDestFieldMixin:
    """:meta private:"""

    def set_dest_field(self, field):
        """:meta private:"""

        self.dest_field = field
        return self
