def check_required_non_negative_float(value: float, param_name: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{param_name} must be a number, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"{param_name} must be non-negative, got {value}")
    return value
