-- a script thatlists all records with score >= 10 in second_table of database hbtn_0c_0 in mysql server
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
