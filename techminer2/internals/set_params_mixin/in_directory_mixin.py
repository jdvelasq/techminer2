"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class InDirectoryMixin:
    """:meta private:"""

    def in_directory(self, directory):
        """:meta private:"""

        self.in_directory = directory
        return self
