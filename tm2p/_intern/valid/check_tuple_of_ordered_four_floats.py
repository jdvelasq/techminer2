from typing import Tuple


def check_tuple_of_ordered_four_floats(
    value: Tuple[float, float, float, float], param_name: str
) -> Tuple[float, float, float, float]:
    if not isinstance(value, tuple) or len(value) != 4:
        raise TypeError(
            f"{param_name} must be a tuple of four floats, got {type(value).__name__} with length {len(value) if isinstance(value, tuple) else 'N/A'}"
        )
    for i, v in enumerate(value):
        if not isinstance(v, float):
            raise TypeError(
                f"{param_name}[{i}] must be a float, got {type(v).__name__}"
            )
    if not value[0] <= value[1] <= value[2] <= value[3]:
        raise ValueError(
            f"{param_name} values must be ordered: {value[0]} ≤ {value[1]} ≤ {value[2]} ≤ {value[3]}"
        )
    return value
