"""
Setup logging using logzero
"""

import datetime
import os

import logzero


def get_logfile_name(log_dir: str) -> str:
    """returns the file name for logs"""
    dt_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return os.path.join(log_dir, f"log-{dt_string}.log")


def setup_logger(log_dir: str, log_level: str) -> None:
    """Create log file and setup logzero"""
    logzero.loglevel(log_level)

    if log_dir is not None:
        logzero.logfile(get_logfile_name(log_dir))
    else:
        logzero.logger.debug("log_dir not defined")
