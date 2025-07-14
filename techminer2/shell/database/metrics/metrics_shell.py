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
from .general.general_shell import GeneralShell


class MetricsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:metrics")

    def do_general(self, arg):
        """Analyze general database metrics."""
        GeneralShell().cmdloop()
