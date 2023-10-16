"""Parameter classes definition"""


class RootDirMixin:
    """Mixin class for root_dir parameter"""

    def __init__(
        self,
        #
        # PROJECT DIRECTORY
        root_dir: str = "./",
    ):
        self._root_dir = root_dir

    @property
    def root_dir(self):
        """Root directory"""
        return self._root_dir


class DatabaseMixin(RootDirMixin):
    """Mixin class for database parameters"""

    def __init__(
        self,
        #
        # DATABASE PARAMS
        root_dir: str = "./",
        database: str = "main",
        year_filter: tuple = (None, None),
        cited_by_filter: tuple = (None, None),
        **filters,
    ):
        super().__init__(root_dir=root_dir)
        self._database = database
        self._year_filter = year_filter
        self._cited_by_filter = cited_by_filter
        self._filters = filters

    @property
    def database(self):
        """Database name"""
        return self._database

    @property
    def year_filter(self):
        """Year filter"""
        return self._year_filter

    @property
    def cited_by_filter(self):
        """Cited by filter"""
        return self._cited_by_filter

    @property
    def filters(self):
        """Filters"""
        return self._filters
