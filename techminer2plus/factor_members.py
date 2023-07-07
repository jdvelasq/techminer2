# flake8: noqa
# pylint: disable=line-too-long
"""
.. _factor_members:

Factor Members
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> cooc_matrix = tm2p.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> factor_matrix = tm2p.factor_decomposition_kernel_pca(
...     cooc_matrix,
... )

>>> factor_clusters = tm2p.factor_clustering(
...    factor_matrix,
...    n_clusters=4,
... )
>>> factor_clusters.centers_
         DIM_00    DIM_01    DIM_02    DIM_03
CL_0  -1.208127  0.084783 -0.211293  0.140393
CL_1   7.233449  2.578726  1.000000  4.195275
CL_2 -18.210254  1.000000 -9.577849 -2.763019
CL_3  16.498383  3.313048  5.874462  1.000000


>>> print(tm2p.factor_members(factor_clusters).to_markdown())
|    | CL_0                           | CL_1               | CL_2                   | CL_3                   |
|---:|:-------------------------------|:-------------------|:-----------------------|:-----------------------|
|  0 | REGTECH 28:329                 | CHARITYTECH 02:017 | DATA_PROTECTION 02:027 | SMART_CONTRACTS 02:022 |
|  1 | FINTECH 12:249                 | ENGLISH_LAW 02:017 |                        |                        |
|  2 | REGULATORY_TECHNOLOGY 07:037   |                    |                        |                        |
|  3 | COMPLIANCE 07:030              |                    |                        |                        |
|  4 | REGULATION 05:164              |                    |                        |                        |
|  5 | ANTI_MONEY_LAUNDERING 05:034   |                    |                        |                        |
|  6 | FINANCIAL_SERVICES 04:168      |                    |                        |                        |
|  7 | FINANCIAL_REGULATION 04:035    |                    |                        |                        |
|  8 | ARTIFICIAL_INTELLIGENCE 04:023 |                    |                        |                        |
|  9 | RISK_MANAGEMENT 03:014         |                    |                        |                        |
| 10 | INNOVATION 03:012              |                    |                        |                        |
| 11 | BLOCKCHAIN 03:005              |                    |                        |                        |
| 12 | SUPTECH 03:004                 |                    |                        |                        |
| 13 | SEMANTIC_TECHNOLOGIES 02:041   |                    |                        |                        |
| 14 | ACCOUNTABILITY 02:014          |                    |                        |                        |
| 15 | DATA_PROTECTION_OFFICER 02:014 |                    |                        |                        |


"""
import pandas as pd


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_members(
    factor_clusters,
):
    """Factor members"""

    communities = factor_clusters.communities_
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
