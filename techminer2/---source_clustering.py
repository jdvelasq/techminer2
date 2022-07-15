"""
Source Clustering
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> source_clustering(directory).head()
                     no  OCC  cum_OCC  global_citations  zone
source_abbr                                                  
CEUR WORKSHOP PROC    1    5        5                 2     1
STUD COMPUT INTELL    2    4        9                 3     1
JUSLETTER IT          3    4       13                 0     1
EUR BUS ORG LAW REV   4    3       16                65     1
J BANK REGUL          5    3       19                29     1

>>> from pprint import pprint
>>> pprint(source_clustering(directory).columns.to_list())
['no', 'OCC', 'cum_OCC', 'global_citations', 'zone']


"""
