from importlib.resources import files


def internal__get_system_thesaurus_file_path(thesaurus_file: str) -> str:
    """Get the full path to a system (package) thesaurus file."""
    file_path = files("techminer2.package_data.thesaurus").joinpath(thesaurus_file)
    return str(file_path)
