from veachron.core.constants import LOGGER_NAME
from veachron.presentation import main

import logging.config

# {Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz} [{Level:u3}]  ({SourceContext:1}) {Message:lj}{NewLine}{Exception}

logging.config.dictConfig({
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
})

logger = logging.getLogger(LOGGER_NAME)
pass


if __name__ == '__main__':
    main()
