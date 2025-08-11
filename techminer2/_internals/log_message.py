"""Message output."""
import sys

COUNTER = 0
# with_prompt_flag()


def internal__log_message(
    msgs,
    prompt_flag=False,
    initial_newline=False,
):
    """Prints a log message in the sys.stderr strem."""

    global COUNTER

    if isinstance(msgs, str):
        msgs = [msgs]

    if isinstance(prompt_flag, bool):
        if prompt_flag is True:
            COUNTER += 1
            prefix = f"-- {COUNTER:04d} --"
        else:
            prefix = "-- INFO --"
    else:
        if not isinstance(prompt_flag, int):
            raise ValueError("prompt_flag must be a boolean or an integer.")
        if prompt_flag < 0:
            prefix = "         :"
        else:
            COUNTER = prompt_flag
            prefix = f"-- {COUNTER:04d} --"

    for i_msg, msg in enumerate(msgs):
        if i_msg == 0:
            if initial_newline:
                sys.stderr.write("\n")
            sys.stderr.write(f"{prefix} {msg}\n")
        else:
            sys.stderr.write(f"         : {msg}\n")

    sys.stderr.flush()


# =============================================================================
