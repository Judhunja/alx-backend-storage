-- adds a new correction for a student, and creates a project if it did not exist
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE projectId INT;
    SELECT id INTO projectId FROM projects WHERE project_name = name;
    IF projectId IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SELECT id INTO projectId FROM projects WHERE project_name = name;
        -- alternative to the above line: SET projectId = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, projectId, score);
END;
$$
