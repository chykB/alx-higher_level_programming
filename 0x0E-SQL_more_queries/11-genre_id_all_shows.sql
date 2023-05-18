-- a script that lists all shows contained in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT tv_shows.title, tv_show_genres.genre.id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.titles, tv_show_genres.genre_id;

