"""
Cleaning institutions fields
===============================================================================
"""
# pylint: disable=no-member

from techminer.utils.io import save_records_to_directory
from techminer.utils.map import map_
from techminer.utils.thesaurus import read_textfile

from .utils import load_records_from_directory, logging, save_records_to_directory


def clean_institution_fields(dirpath):
    """
    Cleans all the institution fields in the records in the given directory using the
    institutions thesaurus (institutions.txt file).

    """

    logging.info("Applying thesaurus to institutions ...")

    data = load_records_from_directory(dirpath)

    if dirpath[-1] != "/":
        dirpath = dirpath + "/"

    #
    # Loads the thesaurus
    #
    thesaurus_file = dirpath + "institutions.txt"
    th = read_textfile(thesaurus_file)
    th = th.compile_as_dict()

    #
    # Copy affiliations to institutions
    #
    data["institutions"] = data.affiliations.map(
        lambda w: w.lower().strip(), na_action="ignore"
    )

    #
    # Cleaning
    #
    logging.info("Extract and cleaning institutions.")
    data["institutions"] = map_(
        data, "institutions", lambda w: th.apply_as_dict(w, strict=True)
    )

    logging.info("Extracting institution of first author ...")
    data["institution_1st_author"] = data.institutions.map(
        lambda w: w.split(";")[0] if isinstance(w, str) else w
    )

    save_records_to_directory(records=data, directory=dirpath)

    logging.info("The thesaurus was applied to institutions.")
