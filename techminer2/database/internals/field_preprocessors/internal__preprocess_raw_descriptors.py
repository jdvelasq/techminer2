# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...field_operators.operators__merge_fields import internal__merge_fields


def internal__preprocess_raw_descriptors(root_dir):

    internal__merge_fields(
        source=["raw_nlp_phrases", "raw_keywords"],
        dest="raw_descriptors",
        root_dir=root_dir,
    )
