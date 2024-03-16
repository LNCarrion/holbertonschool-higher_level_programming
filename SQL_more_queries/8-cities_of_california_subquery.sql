-- adding all cities of california
SELECT *
FROM cities
Where state_id = (SELECT iD FROM WHERE name = 'california')
ORDER BY id ASC;