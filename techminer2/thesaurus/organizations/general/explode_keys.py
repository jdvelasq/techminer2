# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Explode Keys
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import InitializeThesaurus, ExplodeKeys

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Explode thesaurus keys
    >>> ExplodeKeys().where_root_directory("examples/fintech/").run()

    >>> from techminer2.thesaurus.organizations import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/small/")
    ... ).run()

"""
from techminer2._internals import ParamsMixin
from techminer2.thesaurus.user import ExplodeKeys as UserExplodeKeys


class ExplodeKeys(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserExplodeKeys()
            .update(**self.params.__dict__)
            .update(
                thesaurus_file="organizations.the.txt",
                root_directory=self.params.root_directory,
            )
            .run()
        )


# =============================================================================
