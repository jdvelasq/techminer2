"""Load thesaurus as reversed dictionary."""

from ._load_thesaurus_as_dict import load_thesaurus_as_dict


# This function loads thesaurus from file and returns it as dictionary.
# Each key is a word and each value is a list of synonyms.


def load_thesaurus_as_dict_r(filename):
    """Returns reversed thesaurus as dictionary."""
    # load thesaurus as dictionary
    thesaurus = load_thesaurus_as_dict(filename)
    # reverse thesaurus
    reversed_thesaurus = {
        value: key for key, values in thesaurus.items() for value in values
    }
    # return reversed thesaurus
    return reversed_thesaurus
