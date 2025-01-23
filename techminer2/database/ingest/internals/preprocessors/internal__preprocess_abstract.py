# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


from ..operators.internal__clean_text import internal__clean_text


def internal__preprocess_abstract(root_dir):
    """:meta private:"""

    internal__clean_text(
        source="raw_abstract",
        dest="abstract",
        root_dir=root_dir,
    )
