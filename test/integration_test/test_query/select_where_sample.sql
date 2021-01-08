SELECT (
    name ,
    surname ,
    age ,
    gender,
    nationality 
) FROM users
WHERE 
    name=? AND 
    surname=?;