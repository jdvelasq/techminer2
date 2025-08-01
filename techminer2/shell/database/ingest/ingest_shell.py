# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

from ...base_shell import BaseShell
from ...colorized_prompt import make_colorized_prompt
from .commands import execute_scopus_command


class IngestShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:ingest")

    def do_scopus(self, arg):
        """Ingest raw data from a Scopus CSV file."""
        execute_scopus_command()
