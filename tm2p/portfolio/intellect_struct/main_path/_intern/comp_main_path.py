import copy
import sys

from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p._intern.helpers.get_zero_digit import get_zero_digits
from tm2p.enum import Field

YEAR = Field.YEAR.value
GCS = Field.GCS.value
LCS = Field.LCS.value
REC_ID = Field.REC_ID.value
LCR = Field.LCR_WOS_FORMAT.value
SHORT_NAME = Field.REC_SHORT_NAME.value


# ------------------------------------------------------------------------------
def step_01_create_citations_table(params):

    sys.stderr.write("  Creating citations table\n")
    sys.stderr.flush()

    #
    # Extracts the records using the specified parameters
    records = load_filtered_main_csv_zip(params=params)

    short_names = dict(
        zip(
            records[REC_ID].to_list(),
            records[SHORT_NAME].to_list(),
        )
    )

    records = records.sort_values(
        [GCS, LCS, YEAR, REC_ID],
        ascending=[False, False, False, True],
    )

    if params.minimum_cited_unit_occurrences is not None:
        records = records.loc[records[GCS] >= params.minimum_cited_unit_occurrences, :]
    if params.top_n_units is not None:
        records = records.head(params.top_n_units)

    #
    # Builds a dataframe with citing and cited articles
    data_frame = records[[REC_ID, LCR, GCS]]

    data_frame.loc[:, LCR] = data_frame[LCR].str.split(";")
    data_frame = data_frame.explode(LCR)
    data_frame[LCR] = data_frame[LCR].str.strip()

    data_frame = data_frame[
        data_frame[LCR].map(lambda x: x in data_frame[REC_ID].to_list())
    ]

    #
    # Adds citations to the article
    _, gcs_digits = get_zero_digits(root_directory=params.root_directory)

    fmt = " 1:{:0" + str(gcs_digits) + "d}"
    #
    rename_dict = {
        key: value
        for key, value in zip(
            records[REC_ID].to_list(),
            (records[REC_ID] + records[GCS].map(fmt.format)).to_list(),
        )
    }
    #
    data_frame[REC_ID] = data_frame[REC_ID].map(rename_dict)
    data_frame[LCR] = data_frame[LCR].map(rename_dict)

    #
    # Creates the citation network
    data_frame = data_frame[[REC_ID, LCR]]
    data_frame = data_frame.rename(
        columns={
            REC_ID: "CITING_DOC",
            LCR: "CITED_DOC",
        }
    )

    data_frame = data_frame.dropna()

    return data_frame, short_names


# ------------------------------------------------------------------------------
def step_02_extracts_main_path_documents(data_frame):

    # Creates the links of the citation network
    data_frame = data_frame.copy()

    #
    # Computes the start nodes in the citation network
    def compute_start_nodes(data_frame):
        data_frame = data_frame.copy()
        return set(data_frame.CITING_DOC.drop_duplicates().tolist()) - set(
            data_frame.CITED_DOC.drop_duplicates().tolist()
        )

    sys.stderr.write("  Computing starting nodes\n")
    sys.stderr.flush()
    start_nodes = compute_start_nodes(data_frame)

    #
    # Computes the end nodes in the citation network
    def compute_end_nodes(data_frame):
        data_frame = data_frame.copy()
        return set(data_frame.CITED_DOC.drop_duplicates().tolist()) - set(
            data_frame.CITING_DOC.drop_duplicates().tolist()
        )

    sys.stderr.write("  Computing ending nodes\n")
    sys.stderr.flush()
    end_nodes = compute_end_nodes(data_frame)

    #
    # Compute paths
    def compute_all_network_paths(data_frame, start_nodes, end_nodes):
        """Computes all possible paths in the citattion network from start nodes to end nodes"""

        # This is a recursive process where new node is added to each path in
        # each iteration until the end node is reached.
        def expand_network_paths(data_frame, end_nodes, found_paths, current_paths):
            """Stack of founded complete paths"""

            found_paths = copy.deepcopy(found_paths)

            new_paths = []

            for current_path in current_paths:
                last_node = current_path[0][-1]

                if last_node in end_nodes:
                    found_paths.append(copy.deepcopy(current_path))
                    continue

                valid_links = data_frame[data_frame.CITING_DOC == last_node].copy()

                for _, row in valid_links.iterrows():

                    if row.CITED_DOC not in current_path[0]:
                        new_path = copy.deepcopy(current_path)
                        new_path[0].append(row.CITED_DOC)
                        new_paths.append(new_path)

            if len(new_paths) > 0:
                found_paths, new_paths = expand_network_paths(
                    data_frame, end_nodes, found_paths, new_paths
                )

            return found_paths, new_paths

        #
        # Main code:
        data_frame = data_frame.copy()
        current_paths = [[[node], 0] for node in start_nodes]
        found_paths, current_paths = expand_network_paths(
            data_frame, end_nodes, [], current_paths
        )
        return found_paths

    sys.stderr.write("  Computing all possible paths\n")
    sys.stderr.flush()
    paths = compute_all_network_paths(data_frame, start_nodes, end_nodes)

    #
    # Computes the points per link in each path
    def compute_points_per_link(data_frame, paths):
        for path in paths:
            for link in zip(path[0], path[0][1:]):
                data_frame.loc[
                    (data_frame.CITING_DOC == link[0])
                    & (data_frame.CITED_DOC == link[1]),
                    "points",
                ] += 1
        return data_frame

    sys.stderr.write("  Computing points per link\n")
    sys.stderr.flush()
    data_frame = data_frame.assign(points=0)
    data_frame = compute_points_per_link(data_frame, paths)

    #
    # Computes the points per path as the sum of points per link
    # in the path
    def compute_points_per_path(data_frame, paths):
        """Computes the points per path."""

        for path in paths:
            for link in zip(path[0], path[0][1:]):
                path[1] += sum(
                    data_frame.loc[
                        (data_frame.CITING_DOC == link[0])
                        & (data_frame.CITED_DOC == link[1]),
                        "points",
                    ]
                )
        return paths

    sys.stderr.write("  Computing points per path\n")
    sys.stderr.flush()
    paths = compute_points_per_path(data_frame, paths)

    #
    # Sort paths by points (descending)
    paths = sorted(paths, key=lambda x: x[1], reverse=True)
    max_points = paths[0][1]

    #
    # Obtains the best paths
    best_paths = [path for path in paths if path[1] == max_points]

    # Creates a subset of documents with only the articles in the best
    # the order of documents_in_main_path is the same as in best_path
    article_in_main_path = set(article for path in best_paths for article in path[0])

    data_frame = data_frame.rename(columns={"points": "POINTS"})

    return article_in_main_path, data_frame


# ------------------------------------------------------------------------------
def step_03_filter_data_frame(data_frame, articles_in_main_path):

    sys.stderr.write("  Filtering records\n")
    sys.stderr.flush()
    data_frame = data_frame[
        (data_frame.CITING_DOC.isin(articles_in_main_path))
        & (data_frame.CITED_DOC.isin(articles_in_main_path))
    ]
    data_frame = data_frame.reset_index(drop=True)
    return data_frame


#
# NOTIFICATIONS:
# -------------------------------------------------------------------------
def internal__notify_process_start():

    sys.stderr.write("Computing Main Path\n")
    sys.stderr.flush()


# -------------------------------------------------------------------------
def internal__notify_process_end():

    sys.stderr.write("  Main Path computed successfully\n")
    sys.stderr.flush()


# ------------------------------------------------------------------------------
def compute_main_path(
    params,
):
    """:meta private:"""

    internal__notify_process_start()

    df, short_names = step_01_create_citations_table(params)
    main_path_docs, df = step_02_extracts_main_path_documents(df)
    df = step_03_filter_data_frame(df, main_path_docs)

    units = set(df["CITING_DOC"].tolist() + df["CITED_DOC"].tolist())
    unit2cit = dict(zip(list(units), [u.split(" ")[-1] for u in units]))
    unit2short = dict(
        zip(
            list(units),
            [
                short_names[" ".join(unit.split(" ")[:-1])] + " " + unit2cit[unit]
                for unit in units
            ],
        )
    )

    df["CITING_DOC"] = df["CITING_DOC"].map(unit2short)
    df["CITED_DOC"] = df["CITED_DOC"].map(unit2short)

    internal__notify_process_end()

    return main_path_docs, df
