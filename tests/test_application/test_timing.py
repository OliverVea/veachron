from pytest import fixture
from core.timing import TimerTree
from application.timing import add_timing_entry, add_timing_exit, list_timings, get_timing_entry_id
import persistence

@fixture(autouse=True)
def empty_timers():
    persistence.timers = {}

def test__get_timing_entry_id__single_call__works_as_expected():
    result = get_timing_entry_id()
    assert len(result) == 20


def test__add_timing_entry__without_timestamp__correct_timestamp_is_added():
    assert True, 'needs to be implemented.'


def test__list_timings__with_tree_of_timers__returns_correct_tree():
    add_timing_entry('A', timer_parent_id=None)
    add_timing_entry('B', timer_parent_id='A')
    add_timing_entry('C', timer_parent_id='A')
    add_timing_entry('D', timer_parent_id='B')
    add_timing_entry('E', timer_parent_id=None)

    timings = list_timings()

    e, a = timings
    c, b = a.children
    d,   = b.children

    nodes = (a, b, c, d, e)

    assert all(type(n) == TimerTree for n in nodes)
    assert all(n.timer_id == e for n, e in zip(nodes, ('A', 'B', 'C', 'D', 'E')))
    assert all(n.parent_id == e for n, e in zip(nodes, (None, 'A', 'A', 'B', None)))
    assert all(len(n.children) == e for n, e in zip(nodes, (2, 1, 0, 0, 0)))


def test__list_timings__with_timers_with_timings__returns_correct_total_time():
    a_a_start, a_a_end = 200, 250
    a_b_start, a_b_end = 500, 560
    b_a_start, b_a_end = 210, 220
    b_b_start, b_b_end = 512, 527

    add_timing_entry(timer_id='A', timer_parent_id=None, timing_id='a', timestamp=a_a_start)
    add_timing_entry(timer_id='A', timer_parent_id=None, timing_id='b', timestamp=a_b_start)
    add_timing_entry(timer_id='B', timer_parent_id='A', timing_id='a', timestamp=b_a_start)
    add_timing_entry(timer_id='B', timer_parent_id='A', timing_id='b', timestamp=b_b_start)
    add_timing_exit(timer_id='A', timing_id='a', timestamp=a_a_end)
    add_timing_exit(timer_id='A', timing_id='b', timestamp=a_b_end)
    add_timing_exit(timer_id='B', timing_id='a', timestamp=b_a_end)
    add_timing_exit(timer_id='B', timing_id='b', timestamp=b_b_end)
    
    timings = list_timings()

    a, = timings
    b, = a.children

    assert a.total_time == a_a_end + a_b_end - a_a_start - a_b_start
    assert b.total_time == b_a_end + b_b_end - b_a_start - b_b_start
