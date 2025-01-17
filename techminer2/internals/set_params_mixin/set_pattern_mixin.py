"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetPatternMixin:
    """:meta private:"""

    def set_pattern(self, pattern):
        """:meta private:"""

        self.pattern = pattern
        return self
