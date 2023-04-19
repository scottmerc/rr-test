"""
Basic logging setup. Use this like:

from logger import logger
logger.info('some message')
"""
from __future__ import absolute_import
import logging
import sys
import os
from platform import system as platform_system


def colorize(data, color):
    colors = {
        'none': "0",
        'black': "0;30",
        'red': "0;31",
        'green': "0;32",
        'brown': "0;33",
        'blue': "0;34",
        'purple': "0;35",
        'cyan': "0;36",
        'light-gray': "0;37",
        'dark-gray': "1:30",
        'light-red': "1;31",
        'light-green': "1;32",
        'yellow': "1;33",
        'light-blue': "1;34",
        'light-purple': "1;35",
        'light-cyan': "1;36",
        'white': "1;37"
    }

    if color not in colors:
        raise Exception("No such color: {}".format(color))

    start = '\033[{}m'.format(colors[color])
    end = '\033[{}m'.format(colors['none'])

    return start + data + end


def default_formatter():
    pid = os.getpid()

    pieces = [
        ('%(asctime)s.%(msecs)03d', 'cyan'),
        ('pid:{}'.format(pid), 'light-red'),
        ('%(filename)-20s %(lineno)4d', 'blue'),
        ('%(levelname)-10s', 'yellow'),
        ('%(message)s', 'green')
    ]

    # platform_system() is 'Windows' on the powershell
    if sys.stderr.isatty() and platform_system() not in ['Windows']:
        # If running in a TTY, show colored output
        fmt = ' '.join([colorize(x[0], x[1]) for x in pieces])
    else:
        # If being directed or piped, show plaintext
        fmt = ' '.join([x[0] for x in pieces])

    return logging.Formatter(fmt, "%b %d %Y %H:%M:%S")


def setup_logger(logger, level=logging.INFO):
    """Basic setup for a given logger. Adds a stderr stream handler with
    default headspin formatting."""
    logger.propagate = False
    logger.setLevel(level)
    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(default_formatter())
    logger.addHandler(handler)


#
# Global logger
#

logger = logging.getLogger('hs_google_play')


def setup(level=logging.INFO):
    """Setup the default logger."""
    setup_logger(logger, level=level)
