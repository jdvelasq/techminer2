# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
from dataclasses import dataclass
from typing import Optional


@dataclass
class AnalysisParams:
    """:meta private:"""

    field: Optional[str] = None


class AnalysisParamsMixin:
    """:meta private:"""

    def set_analysis_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.analysis_params, key):
                setattr(self.analysis_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for AnalysisParams: {key}")
        return self
