"""Report imported records per file"""

import glob
import os

import pandas as pd  # type: ignore

from ._message import message


def report_imported_records_per_file(root_dir):
    """Report the number of imported records per file.

    Args:
        root_dir (str): root directory.

    :meta private:
    """

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        message(f"{file}: {len(data.index)} imported records")
