SELECT * FROM cinema where (id % 2) > 0 AND description NOT IN ('boring') ORDER BY rating DESC;
