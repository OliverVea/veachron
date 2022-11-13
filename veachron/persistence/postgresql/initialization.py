import importlib.resources as resources

import  veachron.persistence.postgresql as postgresql

CREATE_TIMER_TABLE = resources.read_text('veachron.persistence.postgresql.commands', 'create_timer_table.sql')
CREATE_TIMING_TABLE = resources.read_text('veachron.persistence.postgresql.commands', 'create_timing_table.sql')

def initialize_database():
    postgresql.execute(CREATE_TIMER_TABLE)
    postgresql.execute(CREATE_TIMING_TABLE)
    postgresql.commit()

def clear_database():
    postgresql.execute('DROP TABLE IF EXISTS timing, timer')
    postgresql.commit()