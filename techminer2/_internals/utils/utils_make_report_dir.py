"""Creates the report directory for different modules"""
import os.path


def _utils_make_report_dir(root_dir, report_dir):
    """Make report directory."""

    report_path = os.path.join(root_dir, "reports", report_dir)

    if os.path.exists(report_path):
        for root, dirs, files in os.walk(report_path, topdown=False):
            for filename in files:
                if filename.endswith(""):
                    os.remove(os.path.join(root, filename))
            for dirname in dirs:
                if dirname.endswith(""):
                    os.rmdir(os.path.join(root, dirname))
        os.rmdir(report_path)

    os.makedirs(report_path)
