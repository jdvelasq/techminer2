from tm2p import ItemsOrderBy


def check_required_items_order_by_enum(
    value: ItemsOrderBy, param_name: str
) -> ItemsOrderBy:

    if not isinstance(value, ItemsOrderBy):
        raise TypeError(
            f"{param_name} must be an ItemsOrderBy, got {type(value).__name__}"
        )

    return value
