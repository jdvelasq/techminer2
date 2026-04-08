This subpackage implements clustering of the first-order co-occurrence matrix 
using matrix-based clustering methods.

The input is a normalized first-order matrix derived from a co-occurrence 
matrix computed over documents (elementary contexts). Only bounded similarity 
indices are supported for dissimilarity-based clustering.

Valid normalization indices:

    AssociationIndex.JACCARD
    AssociationIndex.DICE
    AssociationIndex.SALTON
    AssociationIndex.EQUIVALENCE
    AssociationIndex.INCLUSION

These indices produce values in [0, 1], allowing the construction of a 
dissimilarity matrix as:

    D = 1 - S

Valid clustering algorithms:

    AgglomerativeClustering     (metric="precomputed", linkage ∈ {"average", "complete", "single"})
    DBSCAN                      (metric="precomputed")
    SpectralClustering          (affinity="precomputed")
    AffinityPropagation         (affinity="precomputed")

Notes:

- AgglomerativeClustering is the canonical method and reproduces the T-LAB workflow.
- DBSCAN is provided as an exploratory density-based alternative.
- SpectralClustering and AffinityPropagation operate directly on the similarity matrix S.
- ASSOCIATION_STRENGTH and MUTUALINFO are excluded from this workflow because they do not produce bounded similarities suitable for D = 1 - S.

