from techminer2 import Field


def internal__check_required_field(value: float, param_name: Field) -> Field:

    if not isinstance(value, Field):
        raise TypeError(f"{param_name} must be a Field, got {type(value).__name__}")

    return value
