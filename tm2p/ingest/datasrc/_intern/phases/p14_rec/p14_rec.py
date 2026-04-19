# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p14_rec(params: Params) -> list[Step]:

    from .s01_rec_no import s01_rec_no
    from .s02_rec_id import s02_rec_id
    from .s03_rec_short_name import s03_rec_short_name

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Assigning REC_NO",
            function=s01_rec_no,
            kwargs=common_kwargs,
            count_message="{count} record numbers assigned",
        ),
        Step(
            name="Assigning REC_ID",
            function=s02_rec_id,
            kwargs=common_kwargs,
            count_message="{count} record IDs assigned",
        ),
        Step(
            name="Assigning REC_SHORT_NAME",
            function=s03_rec_short_name,
            kwargs=common_kwargs,
            count_message="{count} record short IDs assigned",
        ),
    ]
