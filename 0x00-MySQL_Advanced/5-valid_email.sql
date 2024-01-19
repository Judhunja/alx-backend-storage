-- creates a trigger that resets 'valid_email' only when the email has been changed
DELIMITER $$
CREATE TRIGGER reset_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF Old.email != New.email THEN 
        IF NEW.email REGEXP '^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,4}$' THEN        
            SET NEW.valid_email = 1;
        ELSE
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END;
$$
