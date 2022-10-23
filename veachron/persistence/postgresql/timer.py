from veachron.core.timing import Timer, Timing
from veachron.core.constants import LOGGER_NAME

import veachron.persistence.postgresql as postgresql
import importlib.resources as resources
from veachron.persistence.postgresql.timing import set_timings, list_timings, get_timings_for_timer

import logging

logger = logging.getLogger(LOGGER_NAME)

INSERT_TIMER = resources.read_text('veachron.persistence.postgresql.commands', 'insert_timer.sql')

def _map_timer(data: tuple[str] | None, timings: dict[str, Timing] | None = None) -> Timer:
    if not data: return None
    _, timer_id, parent_id, display_name = data
    if not timings: timings = {}
    return Timer(id=timer_id, parent_id=parent_id, display_name=display_name, timings=timings)


def set_timer(timer: Timer) -> None:
    """
    Used to insert a Timer into the database.
    If a timer already exists with the Timer.id, it is updated.
    The Timer.timings are also saved to the timing table.
    """
    insert_data = {'timer_id': timer.id, 'parent_id': timer.parent_id, 'display_name': timer.display_name}
    cursor = postgresql.execute(INSERT_TIMER, insert_data)

    result = postgresql.commit(cursor)

    if not result:
        return

    set_timings(timer.timings.values())


def get_timer(timer_id: str) -> Timer | None:
    query = "SELECT * FROM timer WHERE timer_id=%(timer_id)s"
    data = {'timer_id': timer_id}
    cursor = postgresql.execute(query, data)
    
    if not cursor or cursor.arraysize < 1:
        return None

    timings = get_timings_for_timer(timer_id)
    timer_data = cursor.fetchone()
    timer = _map_timer(timer_data, timings)
    
    return timer


def list_timers() -> list[Timer]:
    query = "SELECT * FROM timer"
    cursor = postgresql.execute(query)
    
    if not cursor or cursor.arraysize < 1:
        return []

    timer_data = cursor.fetchall()
    timers = [_map_timer(data) for data in timer_data]
    
    timings_by_timer_id = list_timings()
    for timer in timers:
        timer.timings = timings_by_timer_id[timer.id] if timer.id in timings_by_timer_id else {}

    logger.info(f'Found {len(timers)} timers in db.')

    return timers   
