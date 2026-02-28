from typing import Optional


def check_optional_positive_int(value: Optional[int], param_name: str) -> Optional[int]:
    if value is None:
        return value
    if not isinstance(value, int):
        raise TypeError(f"{param_name} must be int, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"{param_name} must be positive, got {value}")
    return value
