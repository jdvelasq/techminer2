# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long


from ...prepare.fields.process_field import _process_field


def helper_abstracts_and_titles_to_lower_case(root_dir):
    #
    # This function was only created with the aim of improve noun phrases extraction in the importer
    #

    _process_field(
        source="abstract",
        dest="abstract",
        func=lambda x: x.str.lower(),
        root_dir=root_dir,
    )

    _process_field(
        source="document_title",
        dest="document_title",
        func=lambda x: x.str.lower(),
        root_dir=root_dir,
    )
