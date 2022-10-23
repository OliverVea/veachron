CREATE TABLE IF NOT EXISTS timer
(
    id SERIAL PRIMARY KEY,
    timer_id VARCHAR(255) UNIQUE NOT NULL,
    parent_id VARCHAR(255),
    display_name TEXT,
    FOREIGN KEY (parent_id) REFERENCES timer(timer_id) ON DELETE CASCADE
)