"""Check utils.
"""


def check_integer(param, nullable=True):
    """Check if param is integer."""
    if param is None and nullable:
        return None
    if isinstance(param, int):
        return param
    raise ValueError("param must be None or int")


def check_integer_range(param, nullable=True):
    """Check if param is tuple of integers."""
    if param is None and nullable:
        return None
    if isinstance(param, tuple):
        if len(param) != 2:
            raise ValueError("param must be a tuple with 2 elements")
        if all(isinstance(item, int) for item in param):
            return param
    raise ValueError("param must be None or tuple of integers")
