from veachron.core.timing import Timer
from veachron.core.constants import LOGGER_NAME

import psycopg2
import os
import logging

logger = logging.getLogger(LOGGER_NAME)

_db = None

def get_db_connection():
    try:
        db = psycopg2.connect(
            database='veachron',
            host=os.environ['DB_HOST'], 
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'])
        logger.info('Connected successfully to database!')
        return db

    except psycopg2.OperationalError as e:
        logger.error('Failed connecting to the database with the message:\n%s', e)
        return None

def ensure_db(f):
    def inner(*args, **kwargs):
        global _db

        if not _db:
            _db = get_db_connection()
        
        f(*args, **kwargs)

    return inner

@ensure_db
def get_timer(id: str) -> Timer | None:
    return Timer(str(_db.info))
    pass

@ensure_db
def list_timers() -> list[Timer]:
    pass

@ensure_db
def set_timer(id: str, timer: Timer):
    pass