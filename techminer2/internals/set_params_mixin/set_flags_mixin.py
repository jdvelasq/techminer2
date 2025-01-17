"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetFlagsMixin:
    """:meta private:"""

    def set_flags(self, flags):
        """:meta private:"""

        self.flags = flags
        return self
