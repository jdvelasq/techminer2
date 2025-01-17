"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetCaseMixin:
    """:meta private:"""

    def set_case(self, case):
        """:meta private:"""

        self.case = case
        return self
