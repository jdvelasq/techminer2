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

    def set_output_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.output_params, key):
                setattr(self.output_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for OutputParams: {key}")
        return self
