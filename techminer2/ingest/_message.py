"""Message output with counter."""
# pylint: disable=global-statement

#
# Define a message output with counter
COUNTER = 0


def message(msg):
    """Prints a message with a counter."""

    global COUNTER
    COUNTER += 1
    print(f"-- {COUNTER:03d} -- {msg}")
