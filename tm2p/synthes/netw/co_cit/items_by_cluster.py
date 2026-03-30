"""
ItemsByCluster
===============================================================================

* **CITED_AUTH**

    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthes.netw.co_cit import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_AUTH)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                               0                                  1
    0             Butler T 1:033                     Arner DW 1:107
    1  European Commission 1:028  Financial Conduct Authority 1:037
    2           Buckley RP 1:021                  Zetzsche DA 1:033
    3                  FCA 1:017            Anagnostopoulos I 1:031
    4         Bamberger KA 1:014                     Deloitte 1:026


* **CITED_REF**

    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthes.netw.co_cit import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_REF)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                                               0                                                1
    0  Butler T, 2019, PALGR ST DIG BUS ENA 1:21            Arner DW, 2017, NW J INT LAW BUS 1:50
    1           Baxter LG, 2016, DUKE LAW J 1:14         Anagnostopoulos I, 2018, J ECON BUS 1:31
    2       Bamberger KA, 2010, TEX LAW REV 1:11  Zetzsche DA, 2017, SSRN Electronic Journal 1:16
    3        Buckley RP, 2020, J BANK REGUL 1:10     Arner DW, 2015, SSRN Electronic Journal 1:15
    4        Grassi L, 2022, J IND BUS ECON 1:10           Kavassalis P, 2018, J RISK FINANC 1:13



* **CITED_SRC**

    >>> from tm2p import CoCitationUnit
    >>> from tm2p.synthes.netw.co_cit import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_co_citation_unit(CoCitationUnit.CITED_SRC)
    ...     .having_items_in_top(50)
    ...     .having_citation_threshold(0)
    ...     .having_items_in(None)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                               0                             1
    0              J FINANC 1:95  SSRN Electronic Journal 1:91
    1       REV FINANC STUD 1:80      INT REV FINANC ANAL 1:65
    2  TECHNOL FORECAST SOC 1:57          FINANC RES LETT 1:59
    3      EXPERT SYST APPL 1:52     EUR BUS ORGAN LAW RE 1:51
    4      NW J INT LAW BUS 1:52            J BANK FINANC 1:49




"""

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx import cluster_nx_graph, extract_communities
from tm2p.synthes.netw.co_cit._intern.create_nx_graph import create_nx_graph


class ItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = create_nx_graph(self.params)
        nx_graph = cluster_nx_graph(self.params, nx_graph)
        communities = extract_communities(nx_graph)
        if use_counters is False:
            self.params.counters = False
            for col in communities.columns:
                communities[col] = communities[col].apply(remove_counters)

        return communities
