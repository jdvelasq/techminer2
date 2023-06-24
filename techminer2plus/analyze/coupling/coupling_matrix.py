# flake8: noqa
"""
(Create) Coupling Matrix
===============================================================================

Document coupling matrix

>>> ROOT_DIR = "data/regtech/"
>>> import techminer2plus
>>> coupling_matrix = techminer2plus.analyze.coupling.coupling_matrix(
...     field="author_keywords",
...     top_n=20,
...     root_dir=ROOT_DIR,
... )
>>> coupling_matrix.matrix_.head()
column                                              Anagnostopoulos I, 2018, J ECON BUS, V100, P7  ...  von Solms J, 2021, J BANK REGUL, V22, P152
row                                                                                                ...                                            
Anagnostopoulos I, 2018, J ECON BUS, V100, P7                                                   4  ...                                           0
Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, ...                                              2  ...                                           0
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...                                              3  ...                                           1
Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, ...                                              0  ...                                           1
Buckley RP, 2020, J BANK REGUL, V21, P26                                                        2  ...                                           0
<BLANKLINE>
[5 rows x 39 columns]



# pylint: disable=line-too-long
"""
from ...classes import CouplingMatrix
from ...records import read_records
from ..list_items import list_items


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def coupling_matrix(
    field,
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
    """Coupling Network."""

    def compute_cooc_matrix():
        """Computes the co-occurrence matrix of documents."""

        records = read_records(
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        records["article"] = (
            records["article"]
            + " 1:"
            + records["global_citations"].astype(str)
        )

        # computes the raw groups records
        records = records[[field, "article"]]
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        groups = records.groupby(field).agg({"article": list})

        # filter the records:
        item_list = list_items(
            field=field,
            metric="OCC",
            #
            # Item filters:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        filtered_items = item_list.table_.index.tolist()
        groups = groups[groups.index.isin(filtered_items)]

        matrix_list = groups.rename(columns={"article": "column"})
        matrix_list = matrix_list.assign(row=matrix_list["column"])
        matrix_list = matrix_list.explode("column")
        matrix_list = matrix_list.explode("row")

        matrix_list["OCC"] = 1
        matrix_list = matrix_list.groupby(
            ["row", "column"], as_index=False
        ).aggregate("sum")

        matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)

        return filtered_items, matrix

    selected_topics, cooc_matrix = compute_cooc_matrix()

    couplingmatrix = CouplingMatrix()
    #
    # Results:
    couplingmatrix.matrix_ = cooc_matrix
    couplingmatrix.prompt_ = "TODO"
    couplingmatrix.metric_ = "OCC"
    couplingmatrix.field_ = field
    couplingmatrix.topics_ = selected_topics
    #
    # Item filters:
    couplingmatrix.top_n_ = top_n
    couplingmatrix.occ_range_ = occ_range
    couplingmatrix.gc_range_ = gc_range
    #
    # Database params:
    couplingmatrix.root_dir_ = root_dir
    couplingmatrix.database_ = database
    couplingmatrix.year_filter_ = year_filter
    couplingmatrix.cited_by_filter_ = cited_by_filter
    couplingmatrix.filters_ = filters

    return couplingmatrix
