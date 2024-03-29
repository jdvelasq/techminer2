"""Check utils.
"""

# from .classes import ItemsList, ScientoPyGraph


def check_keywords(param):
    """Check if param is a valid bibliometric metric."""

    valid_fields = [
        "raw_author_keywords",
        "raw_index_keywords",
        "raw_title_words",
        "raw_abstract_words",
        "raw_words",
        "author_keywords",
        "index_keywords",
        "title_words",
        "abstract_words",
        "words",
    ]

    if param not in valid_fields:
        raise ValueError(
            f"Invalid field. Must be one of {', '.join(valid_fields)}."
        )
    return param


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


def check_listview(obj):
    """Check if obj is a ListView instance."""
    from .api.records.list_items import ItemsList

    if not isinstance(obj, ItemsList):
        raise TypeError("`obj` must be a ItemsList instance")
    return obj


def check_impact_metric(param):
    """Check if param is a valid impact metric."""
    if param not in [
        "h_index",
        "g_index",
        "m_index",
    ]:
        raise ValueError(
            "Impact measure must be one of: h_index, g_index, m_index"
        )
    return param


def check_bibliometric_metric(param):
    """Check if param is a valid bibliometric metric."""
    if param not in [
        "g_index",
        "h_index",
        "local_citations",
        "m_index",
        "OCC",
        "OCCGC",
        "global_citations",
    ]:
        raise ValueError(
            "Impact measure must be one of: 'OCC', 'global_citations', "
            "'local_citations', 'h_index', 'g_index', 'm_index'"
        )
    return param
