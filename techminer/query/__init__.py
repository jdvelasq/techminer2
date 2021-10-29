from .counts import (
    count_documents_by_term,
    count_documents_by_year,
    count_global_citations_by_term,
    count_global_citations_by_year,
    count_local_citations_by_term,
    count_local_citations_by_year,
    count_terms_by_column,
    mean_global_citations_by_year,
    mean_local_citations_by_year,
)
from .impact import compute_impact_index
from .top_documents import most_cited_documents
