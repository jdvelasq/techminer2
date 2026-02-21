import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore

from techminer2._internals import Params


def pie_plot(
    params: Params,
    dataframe: pd.DataFrame,
) -> go.Figure:

    fig = px.pie(
        dataframe,
        values=params.items_order_by,
        names=dataframe.index.to_list(),
        hole=params.pie_hole,
        hover_data=dataframe.columns.to_list(),
        title=params.title_text,
    )

    fig.update_traces(textinfo="percent+value")

    fig.update_layout(legend={"y": 0.5})

    return fig
