-- List all records from second_table with a score greater than or equal to 10
-- Display the score and name columns in this order
-- Order the results by score in descending order (highest first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
