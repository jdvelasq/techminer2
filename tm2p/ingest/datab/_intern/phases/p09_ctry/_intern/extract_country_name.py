from tm2p._intern.packag_data import load_builtin_mapping, load_builtin_word_list

from .country_replacements import _COUNTRY_REPLACEMENTS

GEONAME_TO_COUNTRY = load_builtin_mapping("geoname_to_country.json")
COUNTRY_NAMES = load_builtin_word_list("country_names.txt")


def extract_country_name_from_string(affiliation: str) -> str:

    country = _extract_from_last_position(affiliation)
    country = _geoname_to_country(affiliation, country)

    return country


def _geoname_to_country(affiliation, country):

    if country == "[UNKNOWN]":

        last_position = affiliation.split(",")[-1].strip()

        for geoname in GEONAME_TO_COUNTRY.keys():

            ctry = _get_ctry_from_geoname(geoname)

            if last_position == geoname:
                return ctry

            if f", {geoname}." in affiliation:
                return ctry

            if f", {geoname}," in affiliation:
                return ctry

            if affiliation.endswith(f" {geoname}"):
                return ctry

    return country


def _get_ctry_from_geoname(geoname):
    mapped_country = GEONAME_TO_COUNTRY[geoname]
    if isinstance(mapped_country, list):
        ctry = mapped_country[0]
    else:
        ctry = mapped_country

    return ctry


def _extract_from_last_position(affiliation):
    country = affiliation.split(",")[-1].strip()
    for pat, repl in _COUNTRY_REPLACEMENTS:
        country = country.replace(pat, repl)
    if country not in COUNTRY_NAMES:
        country = "[UNKNOWN]"
    return country
