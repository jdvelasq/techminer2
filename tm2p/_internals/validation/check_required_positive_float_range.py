from typing import Tuple


def check_required_positive_float_range(
    range_tuple: Tuple[float, float],
    param_name: str,
) -> Tuple[float, float]:

    min_val, max_val = range_tuple

    for val, bound in zip((min_val, max_val), ("min", "max")):
        if not isinstance(val, float):
            raise TypeError(f"{param_name} {bound} value ({val}) must be a float.")
        if val <= 0:
            raise ValueError(f"{param_name} {bound} value ({val}) must be positive.")

    if min_val > max_val:
        raise ValueError(
            f"{param_name} min ({min_val}) > max ({max_val}). Did you swap them?"
        )

    return (min_val, max_val)
