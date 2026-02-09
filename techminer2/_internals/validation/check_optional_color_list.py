from typing import Any, Optional


def check_optional_color_list(
    value: Optional[list[Any]], param_name: str
) -> Optional[list[Any]]:
    if value is None:
        return value
    if not isinstance(value, list):
        raise TypeError(
            f"{param_name} must be a list of colors, got {type(value).__name__}"
        )
    for i, item in enumerate(value):
        if not isinstance(item, (str, int, float)):
            raise TypeError(
                f"{param_name}[{i}] must be a string or number (valid Plotly color), got {type(item).__name__}"
            )
    return value
