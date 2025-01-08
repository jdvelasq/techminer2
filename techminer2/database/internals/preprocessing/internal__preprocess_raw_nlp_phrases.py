# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...operations.operations__merge_fields import internal__merge_fields


def internal__preprocess_raw_nlp_phrases(root_dir):

    internal__merge_fields(
        sources=[
            "raw_document_title_nlp_phrases",
            "raw_abstract_nlp_phrases",
        ],
        dest="raw_nlp_phrases",
        root_dir=root_dir,
    )
