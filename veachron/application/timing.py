from string import ascii_letters
import veachron.persistence as db
from veachron.core.timing import Timer, Timing, TimerTree

import time
import random
from string import ascii_letters, digits

def get_timing_entry_id():
    population = ascii_letters + digits
    return ''.join(random.choices(population, k=20))

def add_timing_entry(
        timer_id: str,
        timer_parent_id: str | None = None, 
        timing_id: str | None = None, 
        timestamp: float | None = None,
        display_name: str | None = None) -> str:
    
    if not timing_id: timing_id = get_timing_entry_id()
    if not timestamp: timestamp = time.time()

    timer = db.get_timer(timer_id)

    if not display_name: 
        if timer: display_name = timer.display_name
        else: display_name = timer_id
    
    timer = timer if timer else Timer(id=timer_id, parent_id=timer_parent_id, display_name=display_name)
    timer.timings[timing_id] = Timing(id=timing_id, entry=timestamp, timer_id=timer_id)
    db.set_timer(timer)

    return timing_id


def add_timing_exit(
        timer_id: str,
        timing_id: str,
        timestamp: float | None = None):

    if not timestamp: timestamp = time.time()
        
    timer = db.get_timer(timer_id)
    if not timer or not timing_id in timer.timings: return

    timer.timings[timing_id].exit = timestamp
    db.set_timer(timer)


def list_timings(timer_id: str | None = None) -> list[TimerTree]:
    timers_by_id = {timer.id: timer for timer in db.list_timers()}
    timers = lambda: timers_by_id.values()

    for timer in timers():
        print(timer)

    timer_trees_by_id = {timer.id: TimerTree(timer.id, timer.parent_id, timer.display_name, timer.time()) for timer in timers()}
    timer_trees = lambda: timer_trees_by_id.values()
    
    trees = []

    while True:
        parent_ids = {timer_tree.parent_id for timer_tree in timer_trees()}
        leaf_timers = [timer_tree for timer_tree in timer_trees() if not timer_tree.timer_id in parent_ids]

        for leaf_timer in leaf_timers:
            del timer_trees_by_id[leaf_timer.timer_id]

        trees += [leaf_timer for leaf_timer in leaf_timers if not leaf_timer.parent_id]
        leaf_timers = [leaf_timer for leaf_timer in leaf_timers if leaf_timer.parent_id]

        for leaf_timer in leaf_timers:
            timer_trees_by_id[leaf_timer.parent_id].children.append(leaf_timer)
        
        if len(timer_trees_by_id) == 0:
            break

    return trees
