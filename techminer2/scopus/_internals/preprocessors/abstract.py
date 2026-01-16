# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from techminer2.database._internals.operators.highlight import internal__highlight


def _preprocess_abstract(root_dir):

    internal__highlight(
        source="tokenized_abstract",
        dest="abstract",
        root_directory=root_dir,
    )


#
