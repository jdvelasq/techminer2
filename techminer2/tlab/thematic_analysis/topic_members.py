# flake8: noqa
# pylint: disable=line-too-long
"""
Topic Members
===============================================================================

Topic extraction using LDA.






>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

>>> lda = tm2p.topic_extraction_with_lda(
...     field="author_keywords",
...     occ_range=(2, None),
...     n_components=10,
...     root_dir=root_dir,
...  )

>>> print(topic_members(lda).to_markdown())
|    | TH_0                           | TH_1                           | TH_2             |
|---:|:-------------------------------|:-------------------------------|:-----------------|
|  0 | REGTECH 28:329                 | BLOCKCHAIN 03:005              | FINANCE 02:001   |
|  1 | FINTECH 12:249                 | SMART_CONTRACTS 02:022         | REPORTING 02:001 |
|  2 | REGULATORY_TECHNOLOGY 07:037   | ACCOUNTABILITY 02:014          |                  |
|  3 | COMPLIANCE 07:030              | DATA_PROTECTION_OFFICER 02:014 |                  |
|  4 | REGULATION 05:164              | GDPR 02:014                    |                  |
|  5 | ANTI_MONEY_LAUNDERING 05:034   | SANDBOXES 02:012               |                  |
|  6 | FINANCIAL_SERVICES 04:168      |                                |                  |
|  7 | FINANCIAL_REGULATION 04:035    |                                |                  |
|  8 | ARTIFICIAL_INTELLIGENCE 04:023 |                                |                  |
|  9 | RISK_MANAGEMENT 03:014         |                                |                  |
| 10 | INNOVATION 03:012              |                                |                  |
| 11 | SUPTECH 03:004                 |                                |                  |
| 12 | SEMANTIC_TECHNOLOGIES 02:041   |                                |                  |
| 13 | DATA_PROTECTION 02:027         |                                |                  |
| 14 | CHARITYTECH 02:017             |                                |                  |
| 15 | ENGLISH_LAW 02:017             |                                |                  |
| 16 | TECHNOLOGY 02:010              |                                |                  |



>>> nmf = tm2p.topic_extraction_with_nmf(
...     field="author_keywords",
...     occ_range=(2, None),
...     n_components=10,
...     root_dir=root_dir,
...  )

>>> print(topic_members(nmf).to_markdown())
|    | TH_00                          | TH_01                  | TH_02                  | TH_03                          | TH_04                  | TH_05                        | TH_06                       | TH_07             | TH_08                        | TH_09                        |
|---:|:-------------------------------|:-----------------------|:-----------------------|:-------------------------------|:-----------------------|:-----------------------------|:----------------------------|:------------------|:-----------------------------|:-----------------------------|
|  0 | COMPLIANCE 07:030              | REGULATION 05:164      | REGTECH 28:329         | ARTIFICIAL_INTELLIGENCE 04:023 | BLOCKCHAIN 03:005      | FINTECH 12:249               | FINANCIAL_SERVICES 04:168   | INNOVATION 03:012 | REGULATORY_TECHNOLOGY 07:037 | ANTI_MONEY_LAUNDERING 05:034 |
|  1 | ACCOUNTABILITY 02:014          | RISK_MANAGEMENT 03:014 | DATA_PROTECTION 02:027 | CHARITYTECH 02:017             | SMART_CONTRACTS 02:022 | SEMANTIC_TECHNOLOGIES 02:041 | FINANCIAL_REGULATION 04:035 | FINANCE 02:001    |                              |                              |
|  2 | DATA_PROTECTION_OFFICER 02:014 | SUPTECH 03:004         | TECHNOLOGY 02:010      | ENGLISH_LAW 02:017             | SANDBOXES 02:012       |                              |                             |                   |                              |                              |
|  3 | GDPR 02:014                    | REPORTING 02:001       |                        |                                |                        |                              |                             |                   |                              |                              |


"""
import pandas as pd


def topic_members(themes):
    """Topic item members"""

    communities = themes.terms_by_theme_
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
