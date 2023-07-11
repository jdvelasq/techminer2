# flake8: noqa
"""
Coverage
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> tm2p.Records(root_dir=root_dir).coverage(
...     field="author_keywords",
... )
--INFO-- Number of documents : 52
--INFO--   Documents with NA : 11
--INFO--  Efective documents : 52
   min_occ  cum_sum_documents coverage  cum num items
0       28                 28  53.85 %              1
1       12                 28  53.85 %              2
2        7                 33  63.46 %              4
3        5                 36  69.23 %              6
4        4                 39  75.00 %              9
5        3                 39  75.00 %             13
6        2                 39  75.00 %             25
7        1                 41  78.85 %            143


"""
