import pandas as pd  # type: ignore


def internal__compute_corr_matrix(
    params,
    data_matrix,
):
    """:meta private:"""

    df_ = data_matrix.copy()

    corr_matrix = pd.DataFrame(
        0.0,
        columns=df_.columns.to_list(),
        index=df_.columns.to_list(),
    )

    for col in df_.columns:
        for row in df_.columns:
            if col == row:
                corr_matrix.loc[row, col] = 1.0
            else:
                matrix = df_[[col, row]].copy()
                matrix = matrix.loc[(matrix != 0).any(axis=1)]
                matrix = matrix.astype(float)
                sumproduct = matrix[row].mul(matrix[col], axis=0).sum()
                if matrix.shape[0] == 0:
                    corr = 0.0
                elif sumproduct == 0.0:
                    corr = 0.0
                elif matrix.shape[0] == 1:
                    corr = 1.0
                elif matrix.shape[0] > 1:
                    corr = df_[col].corr(
                        other=df_[row], method=params.correlation_method
                    )
                else:
                    corr = 0.0
                corr_matrix.loc[row, col] = corr
                corr_matrix.loc[col, row] = corr

    return corr_matrix
