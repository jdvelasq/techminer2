"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class WithPatternMixin:
    """:meta private:"""

    def with_pattern(self, pattern):
        """:meta private:"""

        self.pattern = pattern
        return self
