INSERT INTO timing(timing_id, timer_id, entry, exit)
VALUES(%(timing_id)s, %(timer_id)s, %(entry)s, %(exit)s)
ON CONFLICT (timer_id, timing_id)
DO UPDATE SET entry=%(entry)s , exit=%(exit)s;