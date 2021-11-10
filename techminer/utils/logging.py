"""
Logging info message.
====


"""
import datetime


def debug(msg):
    """
    Logging warning message.

    :param msg: Warning message.

    """
    print(f"{datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} - DEBUG - {msg}")


def info(msg):
    """
    Logging info message.

    :param msg: Info message.

    """
    print(f"{datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} - INFO - {msg}")


def warning(msg):
    """
    Logging warning message.

    :param msg: Warning message.

    """
    print(
        f"{datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} - WARNING - {msg}"
    )
