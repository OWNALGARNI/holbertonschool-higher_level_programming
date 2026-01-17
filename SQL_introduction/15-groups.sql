-- List each score and how many records have that score
-- The count column is labeled as number and results are ordered by number (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
