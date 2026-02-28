from typing import Optional

from tm2p._intern.valid.check_required_str import check_required_str


def check_optional_str(value: Optional[str], param_name: str) -> Optional[str]:
    if value is None:
        return None
    return check_required_str(value=value, param_name=param_name)
