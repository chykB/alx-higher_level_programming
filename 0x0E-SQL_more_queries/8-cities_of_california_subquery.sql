-- a script that lists all the cities of California that can be found in the datSELECT *
SELECT *
FROM cities
WHERE state_id = (
	SELECT state_id
	FROM states
	WHERE name = 'California'
ORDER BY id;
