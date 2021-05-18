import logging

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'


def configure_logging(*script_loggers):
    formatter = logging.Formatter(LOG_FORMAT, LOG_DATEFORMAT)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    library_logger = logging.getLogger('crawlers')

    for logger in script_loggers + (library_logger,):
        logger.setLevel(logging.DEBUG)
        logger.addHandler(ch)
