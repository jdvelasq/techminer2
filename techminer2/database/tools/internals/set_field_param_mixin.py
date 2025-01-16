# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals


class SetFieldParamMixin:
    """:meta private:"""

    def set_field_param(self, field):
        self.field = field
        return self
