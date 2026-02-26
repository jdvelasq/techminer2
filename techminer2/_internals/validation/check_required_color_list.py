from typing import Any


def check_required_color_list(
    value: tuple[Any, ...], param_name: str
) -> tuple[Any, ...]:
    if not isinstance(value, tuple):
        raise TypeError(
            f"{param_name} must be a tuple of colors, got {type(value).__name__}"
        )
    for i, item in enumerate(value):
        if not isinstance(item, (str, int, float)):
            raise TypeError(
                f"{param_name}[{i}] must be a string or number (valid Plotly color), got {type(item).__name__}"
            )
    return value
