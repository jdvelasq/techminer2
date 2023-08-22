# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Lotka's Law
===============================================================================


>>> from techminer2.performance.plots import lotka_law
>>> lotka = lotka_law(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> lotka.fig_.write_html("sphinx/_static/performance/plots/lotka_law.html")

.. raw:: html

    <iframe src="../../../../_static/performance/plots/lotka_law.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(lotka.df_.to_markdown())
|    |   Documents Written |   Num Authors |   Proportion of Authors |   Theoretical Num Authors |   Prop Theoretical Authors |
|---:|--------------------:|--------------:|------------------------:|--------------------------:|---------------------------:|
|  0 |                   1 |            87 |                   0.853 |                    87     |                      0.735 |
|  1 |                   2 |            13 |                   0.127 |                    21.75  |                      0.184 |
|  2 |                   3 |             2 |                   0.02  |                     9.667 |                      0.082 |


"""
