-- Create user and  Grant all permission
-- Create user_0d_1 user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all permission
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
-- Flush privilage
FLUSH PRIVILAGES;
