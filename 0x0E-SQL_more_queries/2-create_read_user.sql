-- Create user and data base and grant SELECT premission on the database
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select permission
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
