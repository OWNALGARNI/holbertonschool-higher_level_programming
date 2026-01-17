-- List all cities with their state name
-- Display: cities.id - cities.name - states.name, ordered by cities.id (ascending)
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
