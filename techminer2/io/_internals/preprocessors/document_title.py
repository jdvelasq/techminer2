# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from techminer2.io._internals.operators.highlight_descriptors import (
    highlight_descriptors,
)


def _preprocess_document_title(root_dir):

    highlight_descriptors(
        source="tokenized_document_title",
        target="document_title",
        root_directory=root_dir,
    )


#
