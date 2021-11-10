import numpy as np
import pandas as pd


class Co_occurrence_analyzer:
    def __init__(self, coc_matrix):
        self.matrix = coc_matrix

    def heat_map(self, figsize=(6, 6), cmap="Reds"):
        """
        Generates a heat map of the co-occurrence matrix.
        """
        import matplotlib.pyplot as plt

        plt.figure(figsize=figsize)
        plt.imshow(self.matrix, cmap=cmap)
        plt.colorbar()
        plt.show()
