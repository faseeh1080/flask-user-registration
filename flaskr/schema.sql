DROP DATABASE IF EXISTS flask_user_registration_app_database;
CREATE DATABASE flask_user_registration_app_database;
USE flask_user_registration_app_database;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    password_hash VARCHAR(255) NOT NULL
);
