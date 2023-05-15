"""
Thematic evolution plot
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix

>>> tm1 = bibliometrix.conceptual_structure.thematic_map(
...     criterion="author_keywords",
...     topics_length=100,
...     directory=directory,
...     start_year=2016,
...     end_year=2019,
... )
--INFO-- The file 'data/regtech/reports/thematic_map/abstracts/CL_00.txt' was created
--INFO-- The file 'data/regtech/reports/thematic_map/abstracts/CL_01.txt' was created
--INFO-- The file 'data/regtech/reports/thematic_map/abstracts/CL_02.txt' was created
--INFO-- The file 'data/regtech/reports/thematic_map/abstracts/CL_03.txt' was created

>>> tm1.communities_.head()
                         CL_00  ...                                CL_03
0                regtech 9:236  ...            algorithmic process 1:003
1                fintech 6:203  ...  artificial intelligence & law 1:003
2     financial services 2:164  ...               equality of arms 1:003
3             regulation 2:161  ...           knowledge impairment 1:003
4  semantic technologies 2:041  ...                        suptech 1:003
<BLANKLINE>
[5 rows x 4 columns]

>>> tm2 = bibliometrix.conceptual_structure.thematic_map(
...     criterion="author_keywords",
...     topics_length=100,
...     directory=directory,
...     start_year=2020,
...     end_year=2023,
... )
>>> tm2.communities_.head()
                           CL_00  ...                             CL_11
0    anti-money laundering 03:21  ...  analytic hierarchy process 01:02
1  artificial intelligence 03:20  ...       regulatory monitoring 01:02
2              charitytech 02:17  ...                                  
3              english law 02:17  ...                                  
4   counter-terror finance 01:14  ...                                  
<BLANKLINE>
[5 rows x 12 columns]


>>> file_name = "sphinx/_static/bibliometrix__thematic_evolution_plot.html"
>>> bibliometrix.conceptual_structure.thematic_evolution_plot(
...     indicators=[tm1, tm2],
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__thematic_evolution_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go


def thematic_evolution_plot(
    indicators,
):
    """Thematic evolution plot"""

    labels = []
    x = []
    y = []
    delta_x = 0
    delta_y = 0.0

    n_indicators = len(indicators)

    data = []
    counter = 0
    n_clusters = 0
    n_clusters_previous = 0
    for indicator in indicators:
        cluster_table = _get_cluster_table(indicator)

        n_clusters_previous += n_clusters
        n_clusters = cluster_table["group"].max() + 1

        x += [delta_x] * n_clusters
        y += [delta_y] * n_clusters
        delta_x += 1.0 / (n_indicators - 1)
        delta_y += 0.01

        labels += cluster_table[cluster_table.rnk == 1].index.tolist()

        cluster_table["group_index"] = cluster_table["group"] + n_clusters_previous
        counter += len(cluster_table)
        data.append(cluster_table)

    values = {}

    for i in range(1, len(data)):
        left_data = data[i - 1]
        right_data = data[i]

        for left_keyword in left_data.index.to_list():
            if left_keyword in right_data.index.to_list():
                # left_cluster = left_data.loc[left_keyword, "cluster"]
                left_index = left_data.loc[left_keyword, "group_index"]
                left_value = left_data.loc[left_keyword, "value"]

                # right_cluster = right_data.loc[left_keyword, "cluster"]
                right_index = right_data.loc[left_keyword, "group_index"]
                right_value = right_data.loc[left_keyword, "value"]

                value = min(left_value, right_value)
                key = (left_index, right_index)
                if key not in values:
                    values[key] = value
                else:
                    values[key] += value

    source = [key1 for (key1, _) in values]
    target = [key2 for (_, key2) in values]
    value = [values[(key1, key2)] for (key1, key2) in values]

    return _make_sankey_plot(labels, x, y, source, target, value)


def _make_sankey_plot(labels, x, y, source, target, value):
    fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node={
                "label": labels,
                "x": x,
                "y": y,
                "color": "#333",
            },
            link={
                "source": source,
                "target": target,
                "value": value,
            },
        )
    )

    fig.update_layout(
        hovermode="x",
        font=dict(size=10, color="black"),
    )

    return fig


def _get_cluster_table(results):
    cluster_table = results.indicators_.copy()

    cluster_table = cluster_table[["group"]]
    cluster_table["value"] = cluster_table.index
    cluster_table.value = cluster_table.value.str.split()
    cluster_table.value = cluster_table.value.map(lambda x: x[-1])
    cluster_table.value = cluster_table.value.str.split(":")
    cluster_table.value = cluster_table.value.map(lambda x: x[0])
    cluster_table.value = cluster_table.value.astype(int)

    index = cluster_table.index.tolist()
    index = [" ".join(i.split()[:-1]) for i in index]
    cluster_table.index = index

    cluster_table["rnk"] = cluster_table.groupby("group")["value"].rank(
        method="first", ascending=False
    )
    cluster_table = cluster_table.sort_values(["group", "rnk"], ascending=[True, False])

    return cluster_table
