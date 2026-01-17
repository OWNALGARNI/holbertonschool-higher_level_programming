-- List all shows and their genre IDs (NULL if no genre is linked)
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Order results by show title and genre ID in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
