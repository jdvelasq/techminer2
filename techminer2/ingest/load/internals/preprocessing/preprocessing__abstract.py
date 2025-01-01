# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


from .....prepare.operations.process_database_field import fields__process
from .preprocessing__clean_text import preprocessing__clean_text


def preprocessing__abstract(root_dir):
    """:meta private:"""

    fields__process(
        source="raw_abstract",
        dest="abstract",
        func=preprocessing__clean_text,
        root_dir=root_dir,
    )
