# flake8: noqa
"""
Factor Grid
===============================================================================

Creates a concept grid from a Factor Matrix.

* **Note:** The number of factors affects the number of columns in the concept grid.

Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> c_grid = techminer2plus.analyze.grid.factor_grid(
...    field='authors',
...    occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> print(c_grid.table_.to_markdown())
|    | CL_00             | CL_01           | CL_02          | CL_03         | CL_04              | CL_05          |
|---:|:------------------|:----------------|:---------------|:--------------|:-------------------|:---------------|
|  0 | Arner DW 3:185    | Brennan R 2:014 | Hamdan A 2:018 | Lin W 2:017   | Grassi L 2:002     | Butler T 2:041 |
|  1 | Buckley RP 3:185  | Crane M 2:014   | Turki M 2:018  | Singh C 2:017 | Lanfranchi D 2:002 | Arman AA 2:000 |
|  2 | Barberis JN 2:161 | Ryan P 2:014    | Sarea A 2:012  |               |                    |                |

>>> #
>>> #  Check:
>>> # 
>>> co_occ_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...     columns='authors',
...     col_occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> m = techminer2plus.analyze.matrix.list_cells_in_matrix(co_occ_matrix).cells_list_
>>> m[m.row < m.column]
                  row              column  OCC
3      Arner DW 3:185    Buckley RP 3:185    3
5   Barberis JN 2:161    Buckley RP 3:185    2
6      Arner DW 3:185   Barberis JN 2:161    2
13     Hamdan A 2:018       Turki M 2:018    2
15      Sarea A 2:012       Turki M 2:018    1
18        Lin W 2:017       Singh C 2:017    2
23    Brennan R 2:014       Crane M 2:014    2
26    Brennan R 2:014        Ryan P 2:014    2
27      Crane M 2:014        Ryan P 2:014    2
29     Hamdan A 2:018       Sarea A 2:012    1
34     Grassi L 2:002  Lanfranchi D 2:002    2


# pylint: disable=line-too-long
"""

import pandas as pd

# from ...classes import ConceptGrid
# from ..matrix.pca_factor_matrix import pca_factor_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_grid(
    obj=None,
    #
    # Specific params:
    field=None,
    threshold=0.5,
    pca=None,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Create clusters from a Factor Matrix."""

    def extract_communities(factor_matrix_):
        """Extracts communities from a factor matrix."""

        groups = []
        table = factor_matrix_.table_.copy()
        table.columns = list(range(len(table.columns)))

        # Generates a list of groups
        columns = table.columns.copy()

        for i_col, col in enumerate(columns):
            # Positive values
            factor = table.loc[table.idxmax(axis=1) == i_col, col]
            group = factor[factor >= threshold].index.tolist()
            if len(group) > 0:
                groups.append(group)
                # remove the elements of group from the rows of factor
                table = table.drop(group)

            # Negative values
            factor = table.loc[table.idxmin(axis=1) == i_col, col]
            group = factor[factor <= -threshold].index.tolist()
            if len(group) > 0:
                groups.append(group)
                table = table.drop(group)

        # Sort groups by length
        groups = sorted(groups, key=len, reverse=True)

        # Converts the groups to a dictionary
        communities = {}
        i_cluster = 0
        for group in groups:
            text = f"CL_{i_cluster:>02d}"
            communities[text] = group
            i_cluster += 1

        return communities

    def sort_community_members(communities):
        """Sorts community members in a dictionary."""

        for key, items in communities.items():
            pdf = pd.DataFrame({"members": items})
            pdf = pdf.assign(
                OCC=pdf.members.map(lambda x: x.split()[-1].split(":")[0])
            )
            pdf = pdf.assign(
                gc=pdf.members.map(lambda x: x.split()[-1].split(":")[1])
            )
            pdf = pdf.sort_values(
                by=["OCC", "gc", "members"], ascending=[False, False, True]
            )
            communities[key] = pdf.members.tolist()

        return communities

    if obj is None:
        obj = factor_matrix(
            field=field,
            pca=pca,
            # Item filters:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    communities = extract_communities(obj)
    communities = sort_community_members(communities)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    obj = ConceptGrid()
    obj.table_ = communities
    obj.prompt_ = "TODO"

    return obj
