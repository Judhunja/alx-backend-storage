-- creates a table with country key having enumerable values
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM("US", "CO", "TN") DEFAULT "US",
    PRIMARY KEY(id)
);
