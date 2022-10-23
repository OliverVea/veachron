INSERT INTO timer(timer_id, parent_id, display_name) 
VALUES(%(timer_id)s, %(parent_id)s, %(display_name)s)
ON CONFLICT (timer_id)
DO UPDATE SET display_name = %(display_name)s;
