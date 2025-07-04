# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface."""

import cmd


class CountriesCLI(cmd.Cmd):
    intro = "Type help or ? to list commands.\n"
    prompt = "(countries) "

    # Submenu commands

    def do_back(self, arg):
        """Go back to the main menu."""
        return True
