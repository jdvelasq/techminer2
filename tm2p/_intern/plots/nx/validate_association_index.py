def validate_association_index(association_index: str):

    valid_indices = [
        "JACCARD",
        "DICE",
        "SALTON",
        "EQUIVALENCE",
        "INCLUSION",
    ]

    if association_index not in valid_indices:
        raise ValueError(
            f"This association index is not supported for clustering. Valid options are: {', '.join(valid_indices)}"
        )
