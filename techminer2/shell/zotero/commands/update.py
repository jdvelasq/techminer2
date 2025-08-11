from techminer2.shell.colorized_input import colorized_input
from techminer2.zotero.export_record_no_to_zotero import ExportRecordNoToZotero


def execute_update_command():

    print()

    zotero_api_key = colorized_input(". Zotero api key [*] > ").strip()
    if zotero_api_key == "":
        zotero_api_key = "MifzqqRsPK5OHvmNoW4Y9Zre"

    zotero_library_id = colorized_input(". Zotero library ID > ").strip()
    if zotero_library_id == "":
        print()
        return

    print()
    (
        ExportRecordNoToZotero()
        .using_zotero_api_key(zotero_api_key)
        .using_zotero_library_id(zotero_library_id)
        .using_zotero_library_type("group")
        .where_root_directory_is("./")
        .run()
    )
