"""Load thesaurus as reversed dictionary."""

from .load_thesaurus_as_dict import load_thesaurus_as_dict


def load_thesaurus_as_dict_r(filename):
    """Returns reversed thesaurus as dictionary."""
    dic = load_thesaurus_as_dict(filename)
    dic = {value: key for key, values in dic.items() for value in values}
    return dic
