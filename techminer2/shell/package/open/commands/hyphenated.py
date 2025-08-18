import subprocess
from importlib.resources import files


def execute_hyphenated_command():

    print()

    file_path = files("techminer2.package_data.text_processing.data").joinpath(
        "hyphenated_is_correct.txt"
    )
    file_path = str(file_path)

    try:
        # Use the `code` command to open the file in VS Code
        subprocess.run(["code", file_path], check=True)
    except FileNotFoundError:
        print("VS Code command-line tool ('code') is not installed or not in PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open file in VS Code: {e}")
