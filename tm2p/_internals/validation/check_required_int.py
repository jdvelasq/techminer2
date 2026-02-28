def check_required_int(value, param_name: str) -> int:

    if not isinstance(value, int):
        raise ValueError(f"{param_name} must be an integer, got {type(value).__name__}")
    return value
