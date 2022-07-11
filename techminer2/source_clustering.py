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
from ._read_records import read_records


def source_clustering(
    directory="./",
    database="documents",
):
    """Source clustering throught Bradfors's Law."""

    records = read_records(directory=directory, database=database, use_filter=False)

    indicators = records[["source_abbr", "global_citations"]]
    indicators = indicators.assign(OCC=1)
    indicators = indicators.groupby(["source_abbr"], as_index=False).sum()
    indicators = indicators.sort_values(by=["OCC", "global_citations"], ascending=False)
    indicators = indicators.assign(cum_OCC=indicators["OCC"].cumsum())
    indicators = indicators.assign(no=1)
    indicators = indicators.assign(no=indicators.no.cumsum())

    cum_occ = indicators["OCC"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(
        indicators.cum_OCC >= int(cum_occ * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(indicators.cum_OCC >= int(cum_occ / 3), 1)
    indicators = indicators.set_index("source_abbr")
    indicators = indicators[["no", "OCC", "cum_OCC", "global_citations", "zone"]]

    return indicators
