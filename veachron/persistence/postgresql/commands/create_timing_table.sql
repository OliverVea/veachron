CREATE TABLE IF NOT EXISTS timing
(
    id SERIAL PRIMARY KEY,
    timing_id VARCHAR(255) NOT NULL,
    timer_id VARCHAR(255) NOT NULL,
    entry DOUBLE PRECISION,
    exit DOUBLE PRECISION,
    FOREIGN KEY (timer_id) REFERENCES timer(timer_id) ON DELETE CASCADE,
    UNIQUE (timing_id, timer_id)
)