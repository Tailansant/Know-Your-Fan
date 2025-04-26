CREATE DATABASE IF NOT EXISTS furia_db;
USE furia_db;

CREATE TABLE IF NOT EXISTS fans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    username VARCHAR(50),
    location VARCHAR(100),
    preferences JSON
);

INSERT INTO fans (name, username, location, preferences) VALUES
('João Silva', 'joaocs', 'São Paulo', '{"CS2": 9, "LoL": 5, "Valorant": 6}'),
('Maria Souza', 'mariagame', 'Rio de Janeiro', '{"CS2": 5, "LoL": 9, "Valorant": 7}'),
('Carlos Lima', 'carlim', 'Belo Horizonte', '{"CS2": 8, "LoL": 3, "Valorant": 10}');
