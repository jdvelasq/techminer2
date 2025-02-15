# pylint: disable=global-statement
"""Message output with counter."""
# import logging
import sys

#
# Define a message output with counter
COUNTER = 0

# logging.basicConfig(level=logging.INFO, format="%(message)s")
# logger = logging.getLogger(__name__)


def log_info_message(msg):
    """Prints a message with a counter."""

    global COUNTER
    COUNTER += 1
    # logger.info(f"-- {COUNTER:03d} -- {msg}")
    sys.stderr.write(f"-- {COUNTER:03d} -- {msg}\n")
    sys.stderr.flush()
