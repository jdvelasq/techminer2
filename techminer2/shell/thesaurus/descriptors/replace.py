# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ...basecli import BaseCLI


class RemoveCLI(BaseCLI):
    prompt = "tm2 > descriptors > remove > "

    # Sub-submenu commands
    def do_prefixes(self, arg):
        """Remove common prefixes from keys."""
        print("Removing prefixes from keys...")
        # Add your removing logic here

    def do_suffixes(self, arg):
        """Remove common suffixes from keys."""
        print("Removing suffixes from keys...")
        # Add your removing logic here

    def do_determiners(self, arg):
        """Remove common determiners from keys."""
        print("Removing determiners from keys...")

    def do_stopwords(self, arg):
        """Remove initial stopwords from keys."""
        print("Removing stopwords from keys...")

    def do_parentheses(self, arg):
        """Remove parentheses from keys."""
        print("Removing parentheses from keys...")

    # --- Back command ---
    def do_back(self, arg):
        """Go back to the previous menu."""
        print("Returning to the thesaurus menu...")
        return True
