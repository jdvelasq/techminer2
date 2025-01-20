# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


class ForFieldSearchPatternMixin:
    """:meta private:"""

    def for_field(
        self,
        with_name: str,
        with_terms_having_pattern: str,
    ):
        self.with_name = with_name
        self.with_terms_having_pattern = with_terms_having_pattern
        return self
