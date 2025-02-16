# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


from .....internals.log_message import internal__log_message
from ..operators.clean_text import internal__clean_text


def internal__preprocess_abstract(root_dir):
    """:meta private:"""

    internal__log_message(
        msgs="Cleaning 'abstract' column.",
        counter_flag=True,
    )

    internal__clean_text(
        source="raw_abstract",
        dest="abstract",
        root_dir=root_dir,
    )
