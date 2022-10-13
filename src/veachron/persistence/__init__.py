from veachron.core.timing import Timer

timers: dict[str, Timer] = {}

def set_timer(timer: Timer) -> None:
    timers[timer.id] = timer

def get_timer(timer_id: str) -> Timer | None:
    return timers.get(timer_id, None)

def list_timers() -> list[Timer]:
    return list(timers.values())