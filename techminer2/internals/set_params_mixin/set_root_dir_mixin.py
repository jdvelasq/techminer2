"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class SetRootDirMixin:
    """:meta private:"""

    def set_root_dir(self, root_dir):
        """:meta private:"""

        self.root_dir = root_dir
        return self
