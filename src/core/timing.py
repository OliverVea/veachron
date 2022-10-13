from __future__ import annotations

from dataclasses import dataclass, field

@dataclass
class Timing:
    id: str
    entry: int
    exit: int | None = None

    def time(self) -> int:
        if self.exit == None: return 0
        return self.exit - self.entry

@dataclass
class Timer:
    id: str
    parent_id: str | None = None
    timings: dict[str, Timing] = field(default_factory=dict)
    display_name: str = ""

    def time(self) -> int:
        return sum(timing.time() for timing in self.timings.values())

@dataclass
class TimerTree:
    timer_id: str
    parent_id: str | None = None
    total_time: int = 0
    children: list[TimerTree] = field(default_factory=list)