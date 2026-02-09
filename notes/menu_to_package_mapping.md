# Menu → Package Mapping (tm2+)

This document maps the user-facing menu structure (notes/menus.txt) to tm2+ subpackages and suggests canonical entry points. It supports GUI/wizard-style classes aligning internal code to competitive software menus.

## INGEST
- Import / Load Data: io, zotero
- Filters (global, dataset-level): io, operations
- Overview (main info panels): explore, metrics
- Sources / Authors / Countries panels: metrics, explore

## REFINE
- Fields (copy/merge/rename/process): io, operations
- Further processing (spaces, counts, extract country/my keywords): text, io, operations
- Search (find records/similar phrases/contexts/KWIC): text, explore
- Thesaurus (abbreviations, descriptors, countries, organizations): thesaurus (canonical), thesaurus_old (legacy)

## ANALYZE
- Citation / Co-citation Networks: networks, metrics, visualization
- Co-occurrence Matrix + Heatmap/Map/Table/Sankey: text, networks, visualization, metrics
- Co-occurrence Network (clusters, concept grid, treemap): networks, clustering, visualization, metrics
- Correlation (auto/cross) matrix & maps: metrics, visualization
- Coupling Network: networks, metrics, visualization
- Document Clustering: clustering, decomposition, topics, visualization
- Documents (selection, top cited refs/docs): io, metrics, explore
- Emergence (emergent topics): topics, metrics, visualization
- Factorial analysis (PCA/NMF; TF‑IDF): decomposition, text, metrics, visualization
- Main path analysis: networks, metrics, visualization
- Metrics (general, terms-by-year frames/plots): metrics, visualization
- RPYS (Reference Publication Year Spectroscopy): metrics, visualization
- Topic modeling (components/documents/themes; mappings): topics, decomposition, visualization
- Tools (associations, cosine graph, radial diagram, word network; coverage, query, statistics, summary): text, metrics, visualization, explore

## REPORT
- Charts (column, bar, pie, line, bubble, butterfly): visualization
- Word cloud / Heat map / Treemap: visualization
- Maps (world map): visualization
- Rankings / Cleveland dot chart: visualization, metrics
- Manuscript/report export: manuscript

## Canonical entry points (suggested)
Define convenience functions (or classes) that emulate menu actions. Place these in operations (pipelines) or techminer2.api for a stable surface.
- ingest_raw_data() → io
- refine_fields_*() → io/operations
- search_concordance_contexts(), search_kwic(), find_similar_records(), highlight_phrase() → text/explore
- apply_thesaurus_*() → thesaurus
- compute_cooccurrence_matrix()/network() → text/networks/metrics
- plot_network(), node_degree_frame()/plot(), node_density_plot() → visualization/networks
- run_document_clustering(), clusters_to_terms_mapping() → clustering/topics
- compute_correlation_matrix()/maps → metrics/visualization
- compute_coupling_network() → networks
- run_factorial_analysis_pca()/nmf() → decomposition
- run_main_path_analysis() → networks/metrics
- compute_metrics_general(), terms_by_year_frame()/plot() → metrics/visualization
- rpys_frame()/plot() → metrics/visualization
- run_topic_modeling_*() → topics/decomposition
- tools_* (associations, coverage, query, statistics, summary) → text/metrics/explore
- report_* (charts, cloud, maps) → visualization/manuscript

## Implementation guidance
- Keep GUI/wizard classes thin: delegate to the canonical entry points above.
- Ensure one function/class per menu action for clarity and testability.
- Re-export common actions in techminer2.api to minimize deep imports.
- Mark legacy modules under _deprecated and route menu actions to canonical implementations.
