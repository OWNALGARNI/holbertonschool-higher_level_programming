-- Create the table force_name if it does not already exist
-- The name column cannot be NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
