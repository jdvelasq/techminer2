# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....internals.log_message import internal__log_message
from ....field_operators.transform_field_operator import internal__transform_field


def internal__preprocess_issn(root_dir):
    """:meta private:"""

    internal__log_message(
        msgs="Processing 'issn' column.",
        prompt_flag=True,
    )

    internal__transform_field(
        field="issn",
        other_field="issn",
        function=lambda x: x,
        root_dir=root_dir,
    )
