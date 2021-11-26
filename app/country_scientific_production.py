import base64
from io import BytesIO

from flask import render_template

from app import app
from techminer import *

directory = "data/"


@app.route("/country_scientific_production")
def country_scientific_production():

    # -------------------------------------------------------------------------
    # World map
    table = column_indicators(directory, "countries")

    fig = world_map(
        table.num_documents,
        cmap="Pastel2",
        figsize=(14, 6),
        title="Country scientific production",
    )
    buf = BytesIO()
    fig.savefig(buf, format="png")
    worldmap_plot = base64.b64encode(buf.getbuffer()).decode("ascii")

    # -------------------------------------------------------------------------

    scientific_production_table = table.copy()

    print(scientific_production_table.to_html(header="true"))
    html = (
        scientific_production_table.to_html(header="true")
        .replace('class="dataframe"', 'class="table table-striped  header-fixed"')
        .replace('style="text-align: right;"', "")
    )

    scientific_production_table = [html]

    # -------------------------------------------------------------------------

    return render_template(
        "country_scientific_production.html",
        title="Country",
        worldmap_plot=worldmap_plot,
        tables=scientific_production_table,
    )
