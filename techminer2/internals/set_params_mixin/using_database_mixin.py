"""Generic Mixin for setting parameters."""

# flake8: noqa
# pylint: disable=too-few-public-methods


class UsingDatabase:
    """:meta private:"""

    def using_database(self, database):
        """:meta private:"""

        self.database = database
        return self
