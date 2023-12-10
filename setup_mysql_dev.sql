-- create a data base in my own server.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_db';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;