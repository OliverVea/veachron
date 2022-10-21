from veachron.core.timing import Timer
import veachron.persistence.postgresql as db

def get_timer(timer_id: str) -> Timer | None:
    db.get_timer(timer_id)

def list_timers() -> list[Timer]:
    return db.list_timers()

def set_timer(timer: Timer) -> None:
    db.set_timer(timer.id, timer)