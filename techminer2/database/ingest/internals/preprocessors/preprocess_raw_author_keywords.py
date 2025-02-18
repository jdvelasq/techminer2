# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


from .....internals.log_message import internal__log_message
from ..operators.clean_raw_keywords import internal__clean_raw_keywords


def internal__preprocess_raw_author_keywords(root_dir):
    """Run importer."""

    internal__log_message(
        msgs="Cleaning 'raw_author_keywords' column.",
        prompt_flag=True,
    )

    internal__clean_raw_keywords(
        source="raw_author_keywords",
        dest="raw_author_keywords",
        root_dir=root_dir,
    )
