"""

>>> from techminer2._constants.country_names import COUNTRY_NAMES
>>> from techminer2._constants.country_to_alpha3 import COUNTRY_TO_ALPHA3
>>> from techminer2._constants.country_to_region import COUNTRY_TO_REGION
>>> from techminer2._constants.country_to_subregion import COUNTRY_TO_SUBREGION

>>> missing_in_names = set(COUNTRY_TO_REGION.keys()) - set(COUNTRY_NAMES)
>>> missing_in_mapping = set(COUNTRY_NAMES) - set(COUNTRY_TO_REGION.keys())
>>> assert not (missing_in_names or missing_in_mapping), (
...     "COUNTRY/Country-to-region mismatch;\\n"
...     f"... missing in COUNTRY_NAMES: {sorted(missing_in_names)};\\n"
...     f"... missing in COUNTRY_TO_REGION: {sorted(missing_in_mapping)}\\n"
... )

>>> missing_in_names = set(COUNTRY_TO_SUBREGION.keys()) - set(COUNTRY_NAMES)
>>> missing_in_mapping = set(COUNTRY_NAMES) - set(COUNTRY_TO_SUBREGION.keys())
>>> assert not (missing_in_names or missing_in_mapping), (
...     "COUNTRY/Country-to-region mismatch;\\n"
...     f"... missing in COUNTRY_NAMES: {sorted(missing_in_names)};\\n"
...     f"... missing in COUNTRY_TO_SUBREGION: {sorted(missing_in_mapping)}\\n"
... )

>>> missing_in_names = set(COUNTRY_TO_ALPHA3.keys()) - set(COUNTRY_NAMES)
>>> missing_in_mapping = set(COUNTRY_NAMES) - set(COUNTRY_TO_ALPHA3.keys())
>>> assert not (missing_in_names or missing_in_mapping), (
...     "COUNTRY/Country-to-region mismatch;\\n"
...     f"... missing in COUNTRY_NAMES: {sorted(missing_in_names)};\\n"
...     f"... missing in COUNTRY_TO_ALPHA3: {sorted(missing_in_mapping)}\\n"
... )



"""
