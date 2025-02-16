"""Message output."""

import sys

COUNTER = 0
# with_counter_flag()


def internal__log_message(
    msgs,
    counter_flag=False,
):
    """Prints a log message in the sys.stderr strem."""

    global COUNTER

    if isinstance(msgs, str):
        msgs = [msgs]

    if isinstance(counter_flag, bool):
        if counter_flag is True:
            COUNTER += 1
            prefix = f"-- {COUNTER:04d} --"
        else:
            prefix = "-- INFO --"
    else:
        if not isinstance(counter_flag, int):
            raise ValueError("counter_flag must be a boolean or an integer.")
        if counter_flag < 0:
            prefix = "         :"
        else:
            COUNTER = counter_flag
            prefix = f"-- {COUNTER:04d} --"

    for i_msg, msg in enumerate(msgs):
        if i_msg == 0:
            sys.stderr.write(f"{prefix} {msg}\n")
        else:
            sys.stderr.write(f"         : {msg}\n")

    sys.stderr.flush()


# =============================================================================
