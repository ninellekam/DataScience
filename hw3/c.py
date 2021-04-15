from time import sleep
import functools
import signal
import sys
import time


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def timeout(seconds):
    def decorator(func):
        if seconds is None or seconds < 0:
            return func

        def handle(signum, frame):
            raise TimeoutException(message='Timed out')
        original_sigalrm_handler = signal.getsignal(signal.SIGALRM)

        @functools.wraps(func)
        def wrapper(*args, **argv):
            signal.signal(signal.SIGALRM, handle)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **argv)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, original_sigalrm_handler)
            return result
        return wrapper
    return decorator
