"""
Network Density Plot
===============================================================================

* **CouplingUnit.AUTH**

.. raw:: html

    <iframe src="../_generated/px.synthes.networks.coupling.kernel_density_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import KernelDensityPlot
    >>> fig = (
    ...     KernelDensityPlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.networks.coupling.kernel_density_plot_auth.html")


* **CouplingUnit.CTRY**

.. raw:: html

    <iframe src="../_generated/px.synthes.networks.coupling.kernel_density_plot_ctry.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import KernelDensityPlot
    >>> fig = (
    ...     KernelDensityPlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.networks.coupling.kernel_density_plot_ctry.html")


* **CouplingUnit.DOC**

.. raw:: html

    <iframe src="../_generated/px.synthes.networks.coupling.kernel_density_plot_doc.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import KernelDensityPlot
    >>> fig = (
    ...     KernelDensityPlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.networks.coupling.kernel_density_plot_doc.html")



* **CouplingUnit.ORG**

.. raw:: html

    <iframe src="../_generated/px.synthes.networks.coupling.kernel_density_plot_org.html"
    height="800px" width="100%" frameBorder="0"></iframe>



Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import KernelDensityPlot
    >>> fig = (
    ...     KernelDensityPlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.networks.coupling.kernel_density_plot_org.html")


* **CouplingUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.synthes.networks.coupling.kernel_density_plot_src.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import CouplingUnit
    >>> from tm2p.synthesize.netw.coupl import KernelDensityPlot
    >>> fig = (
    ...     KernelDensityPlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_coupling_unit(CouplingUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.networks.coupling.kernel_density_plot_src.html")


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import CouplingUnit, ItemOrderBy

from ...._intern.helpers.check_database import check_database

# from tm2p.portfolio.intellectual_structure.coupling_network._intern.doc import (
#     DocKernelDensityPlot,
# )
# from tm2p.portfolio.intellectual_structure.coupling_network._intern.others import (
#     OtherKernelDensityPlot,
# )


class KernelDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        check_database(self.params.root_directory)

        if self.params.coupling_unit == CouplingUnit.DOC:
            DensityPlot = DocKernelDensityPlot
        else:
            DensityPlot = OtherKernelDensityPlot

        return (
            DensityPlot()
            .update(**self.params.__dict__)
            .update(items_order_by=ItemOrderBy.OCC)
            .run()
        )
