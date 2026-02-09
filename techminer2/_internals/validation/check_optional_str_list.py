from typing import List, Optional


def check_optional_str_list(
    value: Optional[List[str]], param_name: str
) -> Optional[List[str]]:
    if value is None:
        return None

    if not isinstance(value, list):
        raise TypeError(f"{param_name} must be a list, got {type(value).__name__}")

    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise TypeError(
                f"All items in {param_name} must be strings. "
                f"Item at index {i} is of type {type(item).__name__}"
            )

    return value
