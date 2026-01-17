-- List all records from second_table where the name is not NULL
-- Display the score and name columns, ordered by score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
