-- Create database and table
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE  hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL);
