"""
Bar
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientopy__bar.html"


>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart

scientopy__bar = bar_chart
