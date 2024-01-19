-- stored procedure that computes and stores average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN u_id INT)
BEGIN
    DECLARE student_score FLOAT;
    SELECT AVG(score) INTO student_score FROM corrections WHERE user_id = u_id;

    IF student_score IS NULL THEN
        SET student_score = 0;
    END IF;
    -- update average_score for student if the student exists on the table
    UPDATE users SET average_score = student_score WHERE id = u_id;
END;
$$
