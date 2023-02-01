"""
Factor Analysis
===============================================================================

Implements a Factor Analysis based on bibliometrix/conceptual_structure/Factor_Analysis.
Source code: 

Algorithm
-------------------------------------------------------------------------------

1. Computes a document-term matrix. Binary if method == "MCA".
2. Applies MCA / CA / MDS to the document-term matrix.
   When the method is MDS computes co-occurrence matrix.
   Always computes 2 components.
3. Applies a clustering algorithm to the previous result
4. Plosts the results.



"""
