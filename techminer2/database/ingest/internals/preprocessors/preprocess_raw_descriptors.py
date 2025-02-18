# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....internals.log_message import internal__log_message
from ....field_operators.merge_fields_operator import internal__merge_fields


def internal__preprocess_raw_descriptors(root_dir):

    internal__log_message(
        msgs="Processing 'raw_descriptors' column.",
        prompt_flag=True,
    )

    internal__merge_fields(
        source=["raw_nouns_and_phrases", "raw_keywords"],
        dest="raw_descriptors",
        root_dir=root_dir,
    )
