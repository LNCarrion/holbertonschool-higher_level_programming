-- creating a data base and giving reaad privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXIST 'usrt_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
Grant SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
