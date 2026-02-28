def check_required_non_negative_int(value: int, param_name: str) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{param_name} must be int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"{param_name} must be non-negative, got {value}")
    return value
