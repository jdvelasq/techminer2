from dataclasses import dataclass
from typing import Optional


@dataclass
class AnalysisParams:
    """:meta private:"""

    item: Optional[str] = None


class AnalysisParamsMixin:

    def set_analysis_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.analysis_params, key):
                setattr(self.analysis_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for AnalysisParams: {key}")
        return self
