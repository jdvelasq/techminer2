from typing import Optional, Union


def check_optional_str_or_dict(
    value: Optional[Union[str, dict]], param_name: str
) -> Optional[Union[str, dict]]:
    if value is None:
        return None
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        raise TypeError(
            f"{param_name} must be a string or a dictionary, got {type(value).__name__}"
        )
    return value
