SELECT (
    name ,
    surname ,
    age ,
    gender,
    nationality 
) FROM sample_table
WHERE 
    name=? AND 
    surname=?;