-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Display NULL if a show doesn’t have a genre.
-- Results must be sorted in ascending order.
SELECT s.`title`, g.`genre_id`
	FROM `tv_shows` AS s
	LEFT JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
	ORDER BY s.`title`, g.`genera_id`;
