-- Write a script that creates the database hbtn_0d_usa 
-- the table states (in the database hbtn_0d_usa) on your MySQL server.
-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database hbtn_0d_usa
use hbtn_0d_usa;
-- script that creates the table states
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);