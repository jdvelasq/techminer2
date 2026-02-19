# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Initialize Thesaurus
===============================================================================


Smoke tests:
    >>> from techminer2.refine.thesaurus_old.user import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory("examples/tests/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )
    INFO: Thesaurus initialized successfully.
      Success : True
      File    : examples/fintech/data/thesaurus/demo.the.txt
      Status  : 1721 keys found
      Header  :
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BETTER_UNDERSTANDING
          A_BETTER_UNDERSTANDING
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
        A_CASE_STUDY
          A_CASE_STUDY
        A_CHALLENGE
          A_CHALLENGE
        A_CLUSTER_ANALYSIS
          A_CLUSTER_ANALYSIS
    <BLANKLINE>

```
python3 - <<'PY'
from techminer2.refine.thesaurus_old.user import InitializeThesaurus
print(
    InitializeThesaurus()
    .with_thesaurus_file("demo.the.txt")
    .with_field("raw_descriptors")
    .where_root_directory("examples/fintech/")
    .run()
)
PY
```

"""


from tqdm import tqdm  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old._internals import ThesaurusMixin, ThesaurusResult

tqdm.pandas()


class InitializeThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def run(self) -> ThesaurusResult:
        """:meta private:"""

        self._build_user_thesaurus_path()
        self.internal__load_filtered_records()
        self.internal__create_thesaurus_data_frame_from_field()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self._sort_data_frame_by_rows_and_key()
        self._write_thesaurus_data_frame_to_disk()

        return ThesaurusResult(
            colored_output=self.params.colored_output,
            file_path=str(self.thesaurus_path),
            msg="Thesaurus initialized successfully.",
            success=True,
            status=f"{self.data_frame.shape[0]} keys found",
            data_frame=self.data_frame,
        )
