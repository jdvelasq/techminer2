import os.path

from . import logging


def save_html_report(directory, html, report_name):
    """Save an HTML report.

    Args:
        directory (str): Path to the directory where the report will be saved.
        html (str): HTML report.
        report_name (str): Name of the report.

    """
    report_path = os.path.join(directory, "reports", report_name)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)
    logging.info(f"Saved HTML report: {report_path}")
