# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
"""Co-occrrence Matrix format params."""

from dataclasses import dataclass


@dataclass
class OutputParams:
    """:meta private:"""

    retain_counters: bool = True


class OutputParamsMixin:
    """:meta private:"""

    def set_format_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.format_params, key):
                setattr(self.format_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for FormatParams: {key}")
        return self
