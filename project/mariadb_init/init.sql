CREATE DATABASE IF NOT EXISTS social_network;

USE social_network;

-- Создание таблицы Account
CREATE TABLE accounts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  login VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  sex ENUM('Male', 'Female'),
  UNIQUE (email), UNIQUE (password), UNIQUE (login)
);

-- Создание таблицы Topic
CREATE TABLE topics (
  id INT AUTO_INCREMENT PRIMARY KEY,
  author_id INT,
  body TEXT NOT NULL,
  date TIMESTAMP NOT NULL,
  change_date TIMESTAMP,
  FOREIGN KEY (author_id) REFERENCES accounts(id)
);

-- Создание таблицы Dialogue
CREATE TABLE dialogues (
  id INT AUTO_INCREMENT PRIMARY KEY,
  account1_id INT,
  account2_id INT,
  created_date TIMESTAMP NOT NULL,
  FOREIGN KEY (account1_id) REFERENCES accounts(id),
  FOREIGN KEY (account2_id) REFERENCES accounts(id),
  UNIQUE KEY (account1_id, account2_id)
);

-- Создание таблицы Message
CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  dialogue_id INT,
  author_id INT,
  body TEXT NOT NULL,
  date TIMESTAMP NOT NULL,
  FOREIGN KEY (dialogue_id) REFERENCES dialogues(id),
  FOREIGN KEY (author_id) REFERENCES accounts(id)
);

-- Заполнение таблицы account
INSERT INTO accounts (login, password, first_name, last_name, email, sex)
VALUES
  ('account1', 'pass1', 'John', 'John', 'john@a.com', 'Male'),
  ('account2', 'pass2', 'Jane', 'Jane', 'jane@a.com', 'Female'),
  ('account3', 'pass3', 'Bob', 'Bob', 'bob@a.com', 'Male');

-- Заполнение таблицы Topic
INSERT INTO topics (body, date, author_id, change_date)
VALUES
  ('Topic 1', NOW(), 1, NULL),
  ('Topic 2', NOW(), 2, NULL),
  ('Topic 3', NOW(), 1, NULL);

-- Заполнение таблицы Dialogue
INSERT INTO dialogues (account1_id, account2_id, created_date)
VALUES
  (1, 2, NOW()),
  (1, 3, NOW()),
  (2, 3, NOW());

-- Заполнение таблицы Message
INSERT INTO messages (dialogue_id, body, author_id, date)
VALUES
  (1, 'Hello!', 1, NOW()),
  (1, 'Hi!', 1, NOW()),
  (2, 'How are you?', 1, NOW());