from __future__ import annotations

from dataclasses import dataclass, field

@dataclass
class Timing:
    id: str
    timer_id: str 
    entry: float
    exit: float | None = None

    def time(self) -> float:
        if self.exit == None: return 0
        return self.exit - self.entry

@dataclass
class Timer:
    id: str
    parent_id: str | None = None
    timings: dict[str, Timing] = field(default_factory=dict)
    display_name: str = ""

    def time(self) -> float:
        return sum(timing.time() for timing in self.timings.values())

@dataclass
class TimerTree:
    timer_id: str
    parent_id: str | None = None
    display_name: str = None,
    total_time: float = 0
    children: list[TimerTree] = field(default_factory=list)

    def __post_init__(self):
        if not self.display_name: self.display_name = self.timer_id

    def to_json(self) -> dict:
        return {
            'timer_id': self.timer_id,
            'parent_id': self.parent_id,
            'total_time': self.total_time,
            'children': [child.to_json() for child in self.children]
        }