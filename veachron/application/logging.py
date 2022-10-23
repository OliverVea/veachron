from veachron.core.constants import LOGGER_NAME

import logging.config

LOGGING_CONFIGURATION = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] (%(module)s:%(lineno)d) %(message)s'
        }
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default', 
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        LOGGER_NAME: {
            'handlers': ['stdout'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

def configure_logging():
    logging.config.dictConfig(LOGGING_CONFIGURATION)