def check_required_bool(value, param_name: str) -> bool:

    if not isinstance(value, bool):
        raise ValueError(f"{param_name} must be a boolean, got {type(value).__name__}")
    return value
