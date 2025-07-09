# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....baseshell import BaseShell


class TranslateCLI(BaseShell):
    prompt = "tm2 > descriptors > translate > "

    def do_ame2bri(self, arg):
        """Translate American English to British English."""
        print("Translating American English to British English...")

    def do_bri2ame(self, arg):
        """Translate British English to American English."""
        print("Translating British English to American English...")

    # --- Back command ---
    def do_back(self, arg):
        """Go back to the previous menu."""
        return True
