"""
Logging info message.
====


"""
import datetime


def logging_info(msg):
    """
    Logging info message.


    """
    print(
        "{} - INFO - {}".format(
            datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), msg
        )
    )
