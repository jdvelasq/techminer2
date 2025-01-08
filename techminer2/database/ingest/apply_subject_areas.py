# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Subject areas


Adds Scopus subject areas to the current database.
"""
import pkg_resources  # type: ignore
import os.path  # type: ignore
import pandas as pd  # type: ignore
import glob  # type: ignore
def apply_subject_areas(
    #
    # DATABASE PARAMS:
    root_dir="./",        
):
    df = _load_subject_areas(root_dir=root_dir)
    subject_areas_by_issn = _compute_subject_areas_by_issn(df)
    subject_areas_by_eissn = _compute_subject_areas_by_eissn(df)

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        data['subject_areas'] = None
        for i_row, row in data.iterrows():
            if not pd.isna(row.issn):
                if row.issn in subject_areas_by_issn:
                    data.loc[i_row, 'subject_areas'] = subject_areas_by_issn[row.issn]
                else:
                    if row.issn in subject_areas_by_eissn:
                        data.loc[i_row, 'subject_areas'] = subject_areas_by_eissn[row.issn]
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


    

def _load_subject_areas(
    #
    # DATABASE PARAMS:
    root_dir="./",        
):

    file_path = pkg_resources.resource_filename(
            "techminer2",
            "subject_areas/_data/subject_areas.csv",
        )
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return pd.read_csv(file_path, encoding="utf-8")


def _compute_subject_areas_by_issn(df):
    df = df.copy()
    df = df[['issn', 'subject_areas']]
    df = df.dropna()
    mapping = dict(zip(df.issn, df.subject_areas))
    return mapping

def _compute_subject_areas_by_eissn(df):
    df = df.copy()
    df = df[['eissn', 'subject_areas']]
    df = df.dropna()
    mapping = dict(zip(df.eissn, df.subject_areas))
    return mapping
