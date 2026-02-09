def check_required_str(value: str, param_name: str) -> str:

    if not isinstance(value, str):
        raise ValueError(f"{param_name} must be a string, got {type(value).__name__}")
    return value
