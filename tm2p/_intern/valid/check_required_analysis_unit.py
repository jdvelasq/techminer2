from tm2p.enum import AnalysisUnit


def check_required_analysis_unit(unit: AnalysisUnit, param_name: str) -> AnalysisUnit:

    if not isinstance(unit, AnalysisUnit):
        raise TypeError(
            f"{param_name} must be a AnalysisUnit, got {type(unit).__name__}"
        )

    return unit
