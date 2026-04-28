from scipy.optimize import curve_fit  # type: ignore

from tm2p.portfolio.perform_metr.annu import Metrics as AnnualMetrics

from .logistic import logistic

OCC = "OCC"
CUMUL_OCC = "CUMUL_OCC"


def compute_model_parameters(params):

    metrics = AnnualMetrics().update(**params.__dict__).run()
    years = metrics.index.values
    annual_counts = metrics[OCC].values
    cumulative = metrics[CUMUL_OCC].values

    fit_result = curve_fit(
        logistic,
        years,
        cumulative,
        p0=[cumulative.max() * 2, 0.3, years.mean()],
        maxfev=10000,
    )
    popt = fit_result[0]
    K, r, t0 = popt

    return K, r, t0, years, annual_counts, cumulative
