-- Create the table id_not_null if it does not already exist
-- The id column has a default value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
