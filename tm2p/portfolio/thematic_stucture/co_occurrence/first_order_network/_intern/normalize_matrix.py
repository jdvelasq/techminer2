import numpy as np
import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import AssociationIndex


def normalize_matrix(
    association_index: AssociationIndex,
    cooc_matrix: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    m = cooc_matrix.astype(float).copy()

    n_docs = len(load_filtered_main_csv_zip(params=params))

    if list(m.index) != list(m.columns):
        raise ValueError("cooc_matrix must be square with identical index/columns.")

    a = m.to_numpy(dtype=float, copy=False)
    diag = np.diag(a).copy()

    if (diag < 0).any():
        raise ValueError("Diagonal frequencies must be nonnegative.")

    if (a < 0).any():
        raise ValueError("Co-occurrence matrix must be nonnegative.")

    if np.any(a > np.minimum(diag[:, None], diag[None, :])):
        raise ValueError("Off-diagonal co-occurrences cannot exceed item frequencies.")

    if (diag > n_docs).any():
        raise ValueError("Diagonal frequencies cannot exceed the number of documents.")

    with np.errstate(divide="ignore", invalid="ignore"):

        # ---------------------------------------------------------------------
        # Used in VOSviewer
        # ---------------------------------------------------------------------
        if association_index == AssociationIndex.ASSOCIATION_STRENGTH:

            den = diag[:, None] * diag[None, :]
            out = np.divide(a, den, out=np.zeros_like(a), where=den != 0)

        # ---------------------------------------------------------------------
        # Used in TLAB
        # ---------------------------------------------------------------------
        elif association_index == AssociationIndex.JACCARD:

            den = diag[:, None] + diag[None, :] - a
            out = np.divide(a, den, out=np.zeros_like(a), where=den != 0)

        elif association_index == AssociationIndex.DICE:

            den = diag[:, None] + diag[None, :]
            num = 2.0 * a
            out = np.divide(num, den, out=np.zeros_like(a), where=den != 0)

        elif association_index in [AssociationIndex.SALTON, AssociationIndex.COSINE]:

            den = np.sqrt(diag[:, None] * diag[None, :])
            out = np.divide(a, den, out=np.zeros_like(a), where=den != 0)

        elif association_index == AssociationIndex.EQUIVALENCE:

            den = diag[:, None] * diag[None, :]
            num = a * a
            out = np.divide(num, den, out=np.zeros_like(a), where=den != 0)

        elif association_index == AssociationIndex.INCLUSION:

            den = np.minimum(diag[:, None], diag[None, :])
            out = np.divide(a, den, out=np.zeros_like(a), where=den != 0)

        elif association_index == AssociationIndex.MUTUALINFO:

            if n_docs <= 0:

                out = np.zeros_like(a)

            else:

                p_ij = a / n_docs
                p_i = diag / n_docs
                den = p_i[:, None] * p_i[None, :]

                out = np.zeros_like(a)
                mask = (p_ij > 0) & (den > 0)
                out[mask] = np.log(p_ij[mask] / den[mask])

        else:
            raise KeyError(f"Unknown association index: {association_index}")

    np.fill_diagonal(out, 0.0)

    return pd.DataFrame(out, index=m.index, columns=m.columns)
