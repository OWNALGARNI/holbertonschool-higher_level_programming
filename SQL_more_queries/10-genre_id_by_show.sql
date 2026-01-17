-- List all shows that have at least one genre linked
-- Display: tv_shows.title and tv_show_genres.genre_id
-- Order by tv_shows.title then tv_show_genres.genre_id (both ascending)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
