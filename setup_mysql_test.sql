-- This script prepares a MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Give hbnb_test all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* to 'hbnb_test'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- Give hbnb_test SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';
