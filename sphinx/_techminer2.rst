User Functions
#########################################################################################

.. raw:: html

   <hr style="height:4px;border-width:0;color:gray;background-color:black">

Data Importation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        import_scopus_file
        import_references
        summary_view

Dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


    .. toctree::
        :maxdepth: 1

        document_viewer
        summary_view
        extract_user_keywords

    .. note::
        VantagePoint uses the title view to select a record for viewing. ``document_viewer`` 
        function implements a document search and returns documents ordered by global 
        citations.



    * ``TODO: The Title View``

    * ``TODO: Create a sub-dataset``

    * ``TODO: Extract Nearby Phrases``

    * ``TODO: Detail Window``





Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        find_string
        stemming
        extract_user_keywords


Thesaurus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1
        
        clean_institutions
        clean_keywords


    .. toctree::
        :maxdepth: 1

        apply_thesaurus
        create_thesaurus


Abstract
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        abstract_concordances
        abstract_screening
        abstract_summarization



Column (Report) Charts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        column_cleveland_dot_chart
        column_horizontal_bar_chart
        column_line_chart
        column_pie_chart
        column_gantt_chart 
        column_tree_map
        column_vertical_bar_chart
        column_word_cloud

    .. note::
        The ``World Map`` chart is implemented as `Country Scientific Production <country_scientific_production.html>`__.



    FROM VANTAGE POINT TOOLBAR


    * Cluster Map

    * Matrix Viewer



Co-occurrence Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        co_occurrence_matrix 
        co_occurrence_matrix_associations
        co_occurrence_matrix_bubble_chart
        co_occurrence_matrix_chord_diagram
        co_occurrence_matrix_cluster_mds_map
        co_occurrence_matrix_cluster_tsne_map
        co_occurrence_matrix_ego_graph
        co_occurrence_matrix_ego_network
        co_occurrence_matrix_heatmap
        co_occurrence_matrix_html
        co_occurrence_matrix_manifold
        co_occurrence_matrix_mds_map
        co_occurrence_matrix_topic_associations
        co_occurrence_matrix_topics_comparison_chart
        co_occurrence_matrix_topics_comparison_network        


Co-occurrence Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      co_occurrence_network_communities
      co_occurrence_network_degree_plot
      co_occurrence_network_graph
      co_occurrence_network_indicators



Occurrence Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1  

        occurrence_matrix
        occurrence_matrix_associations
        occurrence_matrix_bubble_chart
        occurrence_matrix_heatmap
        occurrence_matrix_html


    See `Co-occurrence API <_api_co_occurrence.html>`__




Correlation Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        auto_corr_matrix
        auto_corr_matrix_html
        auto_corr_matrix_heatmap


    .. toctree::
        :maxdepth: 1

        cross_corr_matrix
        cross_corr_matrix_html
        cross_corr_matrix_heatmap


    .. toctree::
        :maxdepth: 1

        correlation_map

Factor Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        factor_matrix 


Thematic Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        thematic_analysis_map
        thematic_analysis_partitions
        thematic_analysis_themes

    .. toctree::
        :maxdepth: 1

        emergent_themes_lda_map
        emergent_themes_lda_themes


    .. toctree::
        :maxdepth: 1

        emergent_themes_nmf_map
        emergent_themes_nmf_themes


Thematic Map
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


   .. toctree::
      :maxdepth: 1

      thematic_map_communities
      thematic_map_degree_plot
      thematic_map_indicators
      thematic_map_network


Factorial Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      factorial_analysis_mds_communities
      factorial_analysis_mds_data
      factorial_analysis_mds_map
      factorial_analysis_mds_silhouette_scores

Comparative Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. toctree::
        :maxdepth: 1

        co_occurrence_matrix_svd_map
        tf_idf_matrix_svd_map


Document Coupling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      coupling_matrix
      coupling_network_communities
      coupling_network_degree_plot
      coupling_network_graph


Citation Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


    .. toctree::
        :maxdepth: 1

        co_citation_network_communities
        co_citation_network_degree_plot
        co_citation_network_graph    
        co_citation_network_indicators
        co_citation_matrix    


    .. toctree::
        :maxdepth: 1

        main_path_network



Collaboration Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      collaboration_network_communities
      collaboration_network_degree_plot
      collaboration_network_graph
      collaboration_network_indicators        