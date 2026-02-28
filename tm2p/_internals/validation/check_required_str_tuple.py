def check_required_str_tuple(
    value: tuple[str, ...], param_name: str
) -> tuple[str, ...]:

    if not isinstance(value, tuple):
        raise TypeError(f"{param_name} must be a tuple, got {type(value).__name__}")

    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise TypeError(
                f"All items in {param_name} must be strings. "
                f"Item at index {i} is of type {type(item).__name__}"
            )

    return tuple(value)
