-- Update the score of Bob to 10 in the second_table
-- The update is done using only the name field, not the id
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
