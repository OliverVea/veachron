from veachron.core.timing import Timing
from veachron.core.constants import LOGGER_NAME
import veachron.persistence.postgresql as postgresql

import logging
import importlib.resources as resources

logger = logging.getLogger(LOGGER_NAME)

INSERT_TIMING = resources.read_text('veachron.persistence.postgresql.commands', 'insert_timing.sql')

def _map_timing(data: tuple[str] | None) -> Timing:
    if not data: return None
    _, timing_id, timer_id, entry, exit = data
    return Timing(id=timing_id, timer_id=timer_id, entry=entry, exit=exit)

def set_timings(timings: list[Timing]) -> None:
    data = [{'timing_id': timing.id, 'timer_id': timing.timer_id, 'entry': timing.entry, 'exit': timing.exit} for timing in timings]
    cursor = postgresql.execute_many(INSERT_TIMING, data)
    
    if not cursor: 
        return

    postgresql.commit(cursor)

def list_timings() -> dict[str, dict[str, Timing]]:
    """
    All timings grouped by timer_id and then timing_id.
    """
    query = "SELECT * from timing"
    cursor = postgresql.execute(query)

    if not cursor or cursor.arraysize < 1:
        return []

    timings_data = cursor.fetchall()
    timings = [_map_timing(data) for data in timings_data] # Could be a generator if i didn't do len().

    logger.debug(f'Found {len(timings)} timings in db.')

    cursor.close()

    result = {}
    for timing in timings:
        result.setdefault(timing.timer_id, {})[timing.id] = timing

    return result

def get_timings_for_timer(timer_id: str) -> dict[str, Timing]:
    """
    Timings for the provided timer_id grouped by timing_id.
    """
    query = "SELECT * from timing WHERE timer_id = %(timer_id)s"
    data = {'timer_id': timer_id}
    cursor = postgresql.execute(query, data)

    if not cursor:
        logger.error('Could not list timings from timer. Returning empty list.') 
        return []

    timing_data = cursor.fetchall()
    timings = [_map_timing(data) for data in timing_data]  # Could be a generator if i didn't do len().

    logger.debug(f'Found {len(timings)} timings in db.')

    return {timing.id: timing for timing in timings}
