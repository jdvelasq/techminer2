"""
Trajectories
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.sleeping_beauties import Trajectories  # type: ignore
    >>> df = (
    ...     Trajectories()
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> df.iloc[0:10, 0:10]  # doctest: +NORMALIZE_WHITESPACE
    COLUMNS                                         2006  2007  ...  2014  2015
    ROWS                                                        ...
    Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300     0     0  ...     2     0
    Liu JK, 2020, ENV SCI POLLUT RES 1:00207           0     0  ...     1     1
    Ding ZK, 2016, WASTE MANAG 1:00201                 0     0  ...     1     0
    Ding ZK, 2018, J CLEAN PROD 1:00178                0     0  ...     0     1
    Wang JY/1, 2015, J CLEAN PROD 1:00143              0     0  ...     0     1
    Orji IJ, 2015, COMPUT IND ENG 1:00125              0     0  ...     0     1
    Yuan HP/1, 2012, WASTE MANAG 1:00109               0     0  ...     2     0
    Wei SK, 2012, EUR J OPER RES 1:00105               0     0  ...     1     0
    He L, 2022, WASTE MANAG 1:00091                    0     0  ...     0     0
    Khan S, 2009, ENV MODEL SOFTW 1:00084              0     0  ...     0     0
    <BLANKLINE>
    [10 rows x 10 columns]



"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit  # type: ignore
from tm2p.portfolio.intellect_struct.cit_netw.matrix import (
    Matrix as CitNetwMatrix,  # type: ignore
)


class Trajectories(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = (
            CitNetwMatrix().update(**self.params.__dict__)
            #
            # CITATION UNIT:
            .with_analysis_unit(AnalysisUnit.DOC)
            #
            # COUNTERS:
            .using_counters(True)
            #
            .run()
        )

        years = {col: int(col.split(", ")[1]) for col in df.columns}

        trajectory = (
            df.rename(columns=years)
            .T.groupby(level=0)  # now rows=years, cols=cited docs  # group by year
            .sum()  # citations received per year
            .T  # back to rows=cited docs, cols=years
        )
        trajectory = trajectory.loc[:, sorted(trajectory.columns)]

        year_min = min(trajectory.columns)
        year_max = max(trajectory.columns)
        trajectory = trajectory.reindex(
            columns=range(year_min, year_max + 1),
            fill_value=0,
        )

        return trajectory
