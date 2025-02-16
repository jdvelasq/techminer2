# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....internals.log_message import internal__log_message
from ....field_operators.transform_field_operator import internal__transform_field


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


def internal__preprocess_source_title(root_dir):
    """:meta private:"""

    internal__log_message(
        msgs="Processing 'source_title' column.",
        counter_flag=True,
    )

    internal__transform_field(
        field="raw_source_title",
        other_field="source_title",
        function=_local_processing_func,
        root_dir=root_dir,
    )
