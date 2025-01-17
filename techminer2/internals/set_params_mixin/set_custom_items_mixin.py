"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetCustomItemsMixin:
    """:meta private:"""

    def set_custom_items(self, custom_items):
        """:meta private:"""

        self.custom_items = custom_items
        return self
