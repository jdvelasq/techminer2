# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.process_database_field import fields__process


def _local_processing_func(text):
    #
    #              DYNA (Colombia)
    # Sustainability (Switzerland)
    #              npj Clean Water
    # Automotive Engineer (London)
    #
    text = text.str.replace("-", "_", regex=False)
    text = text.str.replace("<.*?>", "", regex=True)
    return text


def preprocessing__source_title(root_dir):
    """:meta private:"""

    fields__process(
        source="raw_source_title",
        dest="source_title",
        func=_local_processing_func,
        root_dir=root_dir,
    )
