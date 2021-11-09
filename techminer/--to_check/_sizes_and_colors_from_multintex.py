def sizes_and_colors_from_multiindex(multiindex):

    # node sizes
    node_sizes = multiindex.get_level_values(1)
    max_node_size = node_sizes.max()
    min_node_size = node_sizes.min()
    node_sizes = 400 + 5000 * (node_sizes - min_node_size) / (
        max_node_size - min_node_size
    )

    node_sussu = multiindex.get_level_values(1)
