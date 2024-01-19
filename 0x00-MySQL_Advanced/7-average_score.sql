-- stored procedure that computes and stores average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE student_score FLOAT;
    SELECT AVG(score) INTO student_score FROM corrections WHERE user_id = user_id;

    IF student_score IS NULL THEN
        SET student_score = 0;
    END IF;
    -- update average_score for student if the student exists on the table
    UPDATE users SET average_score = student_score WHERE id = user_id;

    -- check if a row exists, if not insert the new row
    IF ROW_COUNT() = 0 THEN
        INSERT INTO users (id, average_score) VALUES (user_id, student_score);
    -- alternative that can be used with the above line without the surrounding IF statement: ON DUPLICATE KEY UPDATE average_score = student_score;
    END IF;
END;
$$
