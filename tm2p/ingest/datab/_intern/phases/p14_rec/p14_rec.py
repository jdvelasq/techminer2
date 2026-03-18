# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p14_rec(params: Params) -> list[Step]:

    from .s01_rec_no import s01_rec_no
    from .s02_rec_id import s02_rec_id

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Assigning REC_NO",
            function=s01_rec_no,
            kwargs=common_kwargs,
            count_message="{count} record numbers assigned",
        ),
        Step(
            name="assigning REC_ID",
            function=s02_rec_id,
            kwargs=common_kwargs,
            count_message="{count} record IDs assigned",
        ),
    ]
