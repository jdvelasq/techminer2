# flake8: noqa: F401
# pylint: disable=unused-import, unused-argument

import cmd
import readline
import rlcompleter  # type: ignore

from colorama import Fore, Style, init  # type: ignore

init(autoreset=True)
readline.parse_and_bind("bind ^I rl_complete")

# =============================================================================
#
# Auxiliary functions
#
# =============================================================================


def _colorized_input(prompt):

    prompt = prompt.replace(".", Fore.LIGHTBLACK_EX + "." + Fore.RESET)
    prompt = prompt.replace(">", Fore.LIGHTBLACK_EX + ">" + Fore.RESET)

    return input(prompt).strip()


def _make_colorized_prompt(prompt):

    separator = Fore.LIGHTBLACK_EX + ":" + Style.RESET_ALL

    parts = prompt.split(":")
    parts = [part.strip() for part in parts]
    parts = [
        Fore.LIGHTBLACK_EX + part + Style.RESET_ALL if i != len(parts) - 1 else part
        for i, part in enumerate(parts)
    ]

    colorized_prompt = separator.join(parts)
    colorized_prompt = colorized_prompt + Fore.LIGHTBLACK_EX + " > " + Style.RESET_ALL

    return colorized_prompt


class _BaseShell(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.intro = ""
        self.do_help("")  # Print help on startup

    def do_help(self, arg: str = ""):
        """Help function."""
        if arg:
            try:
                func = getattr(self, f"help_{arg}")
                func()
            except AttributeError:
                print(f"No help available for '{arg}'")
        else:

            print(f"\n{Fore.LIGHTBLACK_EX}Commands:{Style.RESET_ALL}\n")
            commands = [name[3:] for name in self.get_names() if name.startswith("do_")]
            commands = [
                command
                for command in commands
                if command not in ["help", "back", "q", "quit", "exit", "Q"]
            ]
            for command in commands:
                print(
                    f"  {command.ljust(15)} {Fore.LIGHTBLACK_EX}{getattr(self, f'do_{command}').__doc__}{Style.RESET_ALL}"
                )
            print()

    def do_q(self, arg):
        """Go back or exit."""
        print()
        return True

    def do_Q(self, arg):
        """Go back or exit."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        self.do_help("")

    def default(self, line):
        """Handle unknown commands."""
        print()
        print(f"*** Unknown command: <{line}>.")
        self.do_help("")


# =============================================================================
#
# Entry point
#
# =============================================================================


class MainShell(_BaseShell):

    intro = "Welcome. Type help or ? to list commands.\n"

    prompt = _make_colorized_prompt("tm2+")

    def do_ingest(self, arg):
        """Manage ingest operations."""
        IngestShell().cmdloop()
        self.do_help(arg)

    def do_thesaurus(self, arg):
        """Manage thesaurus operations."""
        RefineShell().cmdloop()
        self.do_help(arg)


# =============================================================================
#
# Ingest
#
# =============================================================================


class IngestShell(_BaseShell):

    prompt = _make_colorized_prompt("tm2+:ingest")

    def do_ingest(self, arg):
        """Ingest raw data into the database."""
        IngestShell().cmdloop()
        self.do_help(arg)

    def do_metrics(self, arg):
        """Analyze and compute dataset metrics."""
        # MetricsShell().cmdloop()
        self.do_help(arg)

    def do_search(self, arg):
        """Access the search tools."""
        # SearchShell().cmdloop()
        self.do_help(arg)

    def do_tools(self, arg):
        """Access the tools for data processing."""
        # ToolsShell().cmdloop()
        self.do_help(arg)


# =============================================================================
#
# Refine
#
# =============================================================================


class RefineShell(_BaseShell):

    prompt = _make_colorized_prompt("tm2+:refine")

    def do_acronyms(self, arg):
        """Manage thesaurus for acronyms."""
        # AcronymsShell().cmdloop()
        self.do_help(arg)
