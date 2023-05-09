"""Most frequent items in a databases"""
from dataclasses import dataclass
from ..._plots.bar_plot import bar_plot
from ..._plots.cleveland_plot import cleveland_plot
from ..._plots.column_plot import column_plot
from ..._plots.line_plot import line_plot
from ..._plots.pie_plot import pie_plot
from ..._plots.treemap_plot import treemap_plot
from ...techminer.indicators.indicators_by_topic import indicators_by_topic
from .word_cloud import word_cloud


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None
    prompt_ = None


def chart(
    criterion,
    directory="./",
    database="documents",
    metric="OCC",
    start_year=None,
    end_year=None,
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    title=None,
    plot="bar",
    **filters,
):
    """Generic chart for list plotting."""

    indicators = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if metric == "OCC":
        columns = []
        ascending = []
        if "OCC" in indicators.columns:
            columns.append("OCC")
            ascending.append(False)
        if "global_citations" in indicators.columns:
            columns.append("global_citations")
            ascending.append(False)
        if "local_citations" in indicators.columns:
            columns.append("local_citations")
            ascending.append(False)
        indicators = indicators.sort_values(columns, ascending=ascending)

    if metric == "global_citations":
        columns = []
        ascending = []
        if "global_citations" in indicators.columns:
            columns.append("global_citations")
            ascending.append(False)
        if "local_citations" in indicators.columns:
            columns.append("local_citations")
            ascending.append(False)
        if "OCC" in indicators.columns:
            columns.append("OCC")
            ascending.append(False)
        indicators = indicators.sort_values(columns, ascending=ascending)

    if metric == "local_citations":
        columns = []
        ascending = []
        if "local_citations" in indicators.columns:
            columns.append("local_citations")
            ascending.append(False)
        if "global_citations" in indicators.columns:
            columns.append("global_citations")
            ascending.append(False)
        if "OCC" in indicators.columns:
            columns.append("OCC")
            ascending.append(False)
        indicators = indicators.sort_values(columns, ascending=ascending)

    if custom_topics is None:
        custom_topics = indicators.copy()
        if topic_min_occ is not None:
            custom_topics = custom_topics[custom_topics["OCC"] >= topic_min_occ]
        if topic_min_citations is not None:
            custom_topics = custom_topics[
                custom_topics["global_citations"] >= topic_min_citations
            ]
        custom_topics = custom_topics.index.copy()
        custom_topics = custom_topics[:topics_length]
    else:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]

    indicators = indicators.loc[custom_topics, :]

    plot_function = {
        "bar": bar_plot,
        "cleveland": cleveland_plot,
        "column": column_plot,
        "line": line_plot,
        "pie": pie_plot,
        "treemap": treemap_plot,
        "wordcloud": word_cloud,
    }[plot]

    result = _Results()
    result.table_ = indicators[metric]
    result.plot_ = plot_function(
        dataframe=indicators,
        metric=metric,
        title=title,
    )

    result.prompt_ = f"""
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top {result.table_.shape[0]}
{criterion} with more {metric} in a given bibliographic dataset. 

- 'OCC' is the number of documents published.  

- 'local_citations' are the local citations in the dataset.

- 'global_citations' are the citations received 

{result.table_.to_markdown()}

Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 

Limit your description to a paragraph with no more than 250 words.        
    
"""

    return result
