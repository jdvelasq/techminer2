from tm2p._intern.plots.nx import create_nx_graph_from_matrix_list
from tm2p.enum import Field

from .matrix_list import DocMatrixList as MatrixList

GCS = Field.GCS.value
LCS = Field.LCS.value
YEAR = Field.YEAR.value
RID = Field.REC_ID.value
LCR = Field.LCR_WOS_FORMAT.value
GCR = Field.GCR_WOS_FORMAT.value


def doc_create_nx_graph(params):

    matrix_list = MatrixList().update(**params.__dict__).using_counters(True).run()
    nx_graph = create_nx_graph_from_matrix_list(
        matrix_list.astype({"OCC": float}),
        source="CITED_UNIT",
        target="CITING_UNIT",
        weight="OCC",
    )

    return nx_graph
