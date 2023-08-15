-- Lists all records of the table.
-- Results should display the score and the name listed by descending.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
