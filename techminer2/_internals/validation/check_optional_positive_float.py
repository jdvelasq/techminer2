from typing import Optional


def internal__check_optional_positive_float(
    value: Optional[float], param_name: str
) -> Optional[float]:
    if value is None:
        return value
    if not isinstance(value, float):
        raise TypeError(f"{param_name} must be float, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"{param_name} must be positive, got {value}")
    return value
