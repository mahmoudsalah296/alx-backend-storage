-- script that creates a table users
CREATE TABLE IF NOT EXISTS users(
  id PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE  NOT NULL,
  name VARCHAR(255)
);
