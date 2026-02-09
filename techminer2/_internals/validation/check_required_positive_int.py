def check_required_positive_int(value: int, param_name: str) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{param_name} must be int, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"{param_name} must be positive, got {value}")
    return value
