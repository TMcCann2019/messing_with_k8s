CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

INSERT INTO users (name, email)
VALUES
('Tim', 'tim@example.com'),
('Alice', 'alice@example.com');