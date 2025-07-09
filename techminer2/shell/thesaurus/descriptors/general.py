# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ...baseshell import BaseShell


class GeneralCLI(BaseShell):
    prompt = "tm2 > descriptors > general > "

    # Sub-submenu commands
    def do_apply(self, arg):
        """Apply the thesaurus to the database."""
        print("Applying thesaurus...")
        # Add your applying logic here

    def do_cleanup(self, arg):
        """Cleanup the thesaurus."""
        print("Cleaunp thesaurus...")
        # Add your sorting logic here

    def do_create(self, arg):
        """Reset the thesaurus."""
        print("Sorting thesaurus...")

    def do_integrity(self, arg):
        """Check the integrity of the thesaurus file."""
        print("Sorting thesaurus...")

    def do_reduce(self, arg):
        """Reduce the keys of the thesaurus."""
        print("Reducing thesaurus...")

    # --- Back command ---
    def do_back(self, arg):
        """Go back to the previous menu."""
        print("Returning to the thesaurus menu...")
        return True
