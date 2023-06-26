Techminer2: A package for the analysis of bibliographic datasets using Python
################################################################################

Bibliographic data can be analyzed in various ways, including science mapping 
analysis, technology mining, systematic mapping of literature, bibliometric 
analysis, and scientometric analysis.

To perform these studies, several software tools are available for analyzing 
bibliographic databases. Common options include Bibliometrix, VantagePoint, 
T-LAB, and ScientoPy. However, each tool has its strengths and weaknesses. For 
instance, VantagePoint is powerful for data cleaning but is not open source, 
while Bibliometrix has a friendly user interface but lacks options for data 
cleaning and disambiguation. Similarly, T-LAB excels in text mining but is not 
specifically designed for bibliographic data analysis by fields. The problem 
arises when attempting to conduct a study that combines the strengths of 
multiple software tools. For instance:

* VantagePoint can be used to clean and disambiguate terms.

* Bibliometrix enables the creation of a thematic map using the cleaned author 
  keywords.


* ScientoPy can help identify the cleaned author keywords with a higher average 
  growth rate.


* Lastly, T-LAB can be utilized for topic modeling using the cleaned NLP 
  phrases.

However, in this scenario, a significant amount of time is wasted on exporting 
data from one software to another.


**TechMiner2** is an experimental package designed to facilitate the 
analysis of bibliographic datasets. It aims to support various analysis tasks 
performed by the aforementioned software tools without replacing them. The 
objectives behind its development are:

- Experimenting with data product design strategies, focusing on data-related 
  challenges.

- Experiment with our interpretation of the thecniques implemented in the 
  aforementioned software tools.

- Facilitating the design and experimentation with new algorithms for 
  bibliographic data analysis.

- Assisting in the preparation of MSc and PhD theses, as well as scientific 
  papers based on bibliographic data.

- Providing a platform for the combination and integration of various 
  algorithms available separately in different software tools.

**TechMiner2** features modules that resemble the user interfaces of existing 
software tools, along with additional functionalities inspired by their 
comparison. It is an open-source package distributed under the MIT license 
and is user-friendly, developed and tested in Python version 3.6.

The following figure shows the hierarchical dependencies of the functions.
For example, VantagePoint module depends on the functions of the 
TM2 module.


.. code::

    +--------------+    +--------------+         +--------------+
    |      TM2     |--->| VantagePoint |-------->| Bibliometrix |
    +--------------+    +--------------+         +--------------+
                                |                        |
                                |    +--------------+    | 
                                +--->|    T-LAB     |--->|
                                |    +--------------+    |
                                |                        |
                                |    +--------------+    |
                                +--->|   ScientoPy  |--->+
                                     +--------------+ 


.. toctree::
    :caption: INTRODUCTION
    :hidden:
    :maxdepth: 1

    introduction/getting_started
    introduction/release_info
    introduction/license


.. toctree::
    :caption: USE CASES
    :hidden:
    :maxdepth: 1

    ingest/__index__
    refine/__index__
    find/__index__
    describe/__index__
    analyze/__index__
    
    
    
    


    
    
    
    



**Author**:

    | Prof. Juan David Velásquez-Henao, MSc, PhD
    | Universidad Nacional de Colombia, Sede Medellín.
    | jdvelasq@unal.edu.co


**Indices and Tables**

* :ref:`modindex`

