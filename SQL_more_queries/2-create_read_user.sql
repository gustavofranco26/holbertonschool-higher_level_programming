-- Create hbtn_0d_2 database and the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
