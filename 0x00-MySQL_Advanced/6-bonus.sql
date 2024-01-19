CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE projectName int;
    SELECT COUNT(*) INTO projectName FROM projects WHERE project_name = name;
    IF projectName - 0 THEN
        INSERT IGNORE INTO 
