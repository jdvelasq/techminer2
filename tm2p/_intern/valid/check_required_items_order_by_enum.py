from tm2p.enum import UnitOrderBy


def check_required_unit_order_by_enum(
    value: UnitOrderBy, param_name: str
) -> UnitOrderBy:

    if not isinstance(value, UnitOrderBy):
        raise TypeError(
            f"{param_name} must be an ItemsOrderBy, got {type(value).__name__}"
        )

    return value
