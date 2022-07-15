def _report_duplicate_titles(raw_data, directory):
    duplicates = (
        raw_data.document_title.duplicated(keep=False) & ~raw_data.document_title.isna()
    )
    if duplicates.any():
        file_name = directory + "duplicates.csv"
        duplicates = raw_data[duplicates].copy()
        duplicates = duplicates.sort_values(by=["document_title"])
        duplicates.to_csv(file_name, sep=",", encoding="utf-8", index=False)
        logging.info(
            f"Duplicate rows found in {directory}documents.csv - Records saved to {file_name}"
        )
