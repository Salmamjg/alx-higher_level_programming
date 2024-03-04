-- script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY '1121111sa';
GRANT ALL PRIVILEGES ON sys.* TO 'user_0d_1'@'localhost';