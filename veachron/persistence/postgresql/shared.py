from veachron.core.constants import LOGGER_NAME

import psycopg2
import logging
import os

_db = None
logger = logging.getLogger(LOGGER_NAME)

def _close_db_connection():
    global _db
    try:
        _db.close()
        _db = None
    except Exception as e:
        logger.critical('Failed closing connection to the database with the message:\n%s', e)
        exit()

def _get_db_connection():
    try:
        db = psycopg2.connect(
            database='veachron',
            host=os.environ.get('DB_HOST', 'localhost'), 
            user=os.environ.get('DB_USER', 'user'),
            password=os.environ.get('DB_PASSWORD', 'password'))
        logger.info('Connected successfully to database!')
        return db

    except psycopg2.OperationalError as e:
        logger.error('Failed connecting to the database with the message:\n%s', e)
        return None

def _ensure_db(f):
    def inner(*args, **kwargs):
        global _db

        if not _db:
            _db = _get_db_connection()
        
        return f(*args, **kwargs, db=_db)

    return inner

@_ensure_db
def execute(query: str, data: dict[str, str] = None, cursor = None, db = None):
    """
    Executes the supplied db query with the supplied data.
    Has try-except and requests a cursor.
    Returns db cursor on success and none on failure.
    """
    if not data: data = {}
    q = query
    for key, value in zip(data.keys(), data.values()):
        key = f'%({key})s'
        q = q.replace(key, f'\'{value}\'')
    logger.debug(q)
    try:
        if not cursor: cursor = db.cursor()
        result = cursor.execute(query, data)
        if result: raise Exception(f'Database returned error:\n{result}')
        return cursor
    except Exception as e:
        logger.error('Failed execute with message:\n%s', e)
        _close_db_connection()
        return None

@_ensure_db
def execute_many(query: str, data: list[dict[str, str]] = None, cursor = None, db = None):
    """
    Executes the supplied db queries with the supplied data.
    Has try-except and requests a cursor.
    Returns db cursor on success and none on failure.
    """
    if not data: data = []
    for d in data:
        q = query
        for key, value in zip(d.keys(), d.values()):
            key = f'%({key})s'
            q = q.replace(key, f'\'{value}\'')
        logger.debug(q)

    try:
        if not cursor: cursor = db.cursor()
        result = cursor.executemany(query, data)
        if result: raise Exception(f'Database returned error:\n{result}')
        return cursor
    except Exception as e:
        logger.error('Failed executemany with message:\n%s', e)
        _close_db_connection()
        return None

@_ensure_db
def commit(cursor = None, db = None) -> bool:
    """
    Commits changes to the db and closes the cursor, if provided.
    Returns True on success and False on failure.
    """
    try:
        db.commit()
        if cursor: cursor.close()
        return True
    except Exception as e:
        logger.error('Failed committing changes to db with message:\n%s', e)
        _close_db_connection()
        return False