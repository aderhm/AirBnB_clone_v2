-- create new database if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user if not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges for that user on database created
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select statement on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';