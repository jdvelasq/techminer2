from typing import Tuple, Union


def check_required_positive_number_range(
    range_tuple: Tuple[Union[float, int], Union[float, int]],
    param_name: str,
) -> Tuple[float, float]:

    min_val, max_val = range_tuple

    for val, bound in zip((min_val, max_val), ("min", "max")):
        if not isinstance(val, (float, int)):
            raise TypeError(f"{param_name} {bound} value ({val}) must be a number.")
        if val <= 0:
            raise ValueError(f"{param_name} {bound} value ({val}) must be positive.")

    if min_val > max_val:
        raise ValueError(
            f"{param_name} min ({min_val}) > max ({max_val}). Did you swap them?"
        )

    return (min_val, max_val)
