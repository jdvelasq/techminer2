# CODE_REVIEW: 2026-01-26

from tm2p import CorpusField
from tm2p._internals import Params

from ..step import Step


def build_reference_steps(params: Params) -> list[Step]:

    from ..authors.calculate_numauth import calculate_numauth
    from .assign_recid import assign_recid
    from .assign_recno import assign_recno
    from .calculate_numref_global import calculate_numref_global
    from .compute_citcount_local import compute_citcount_local
    from .normalize_references import normalize_references

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name=f"Assigning '{CorpusField.RNO.value}'",
            function=assign_recno,
            kwargs=common_kwargs,
            count_message="{count} record numbers assigned",
        ),
        Step(
            name=f"Assigning '{CorpusField.RID.value}'",
            function=assign_recid,
            kwargs=common_kwargs,
            count_message="{count} record IDs assigned",
        ),
        Step(
            name=f"Calculating '{CorpusField.N_AUTH.value}'",
            function=calculate_numauth,
            kwargs=common_kwargs,
            count_message="{count} records calculated",
        ),
        Step(
            name=f"Calculating '{CorpusField.N_REF_GBL.value}'",
            function=calculate_numref_global,
            kwargs=common_kwargs,
            count_message="{count} reference counts calculated",
        ),
        Step(
            name=f"Normalizing '{CorpusField.REF_RAW.value}'",
            function=normalize_references,
            kwargs=common_kwargs,
            count_message="{count} references normalized",
        ),
        Step(
            name=f"Compute '{CorpusField.LCS.value}'",
            function=compute_citcount_local,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
    ]


# TODO: _preprocess_references(root_directory)
# TODO: _preprocess_record_id(root_directory)

# TODO: _preprocess_global_references(root_directory)  # ok
# TODO: _preprocess_local_references(root_directory)  # ok
# TODO: _preprocess_local_citations(root_directory)  # ok
# TODO: _preprocess_references(root_directory)
