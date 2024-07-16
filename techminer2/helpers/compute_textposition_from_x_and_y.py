# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np


def compute_textposition_from_x_and_y(node_x, node_y):
    #
    x_mean = np.mean(node_x)
    y_mean = np.mean(node_y)

    textpositions = []
    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition = "top right"
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition = "top left"
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition = "bottom left"
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition = "bottom right"

        textpositions.append(textposition)

    return textpositions
