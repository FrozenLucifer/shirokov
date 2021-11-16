--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Вт ноя 16 23:04:37 2021
--
-- Использованная кодировка текста: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: categoryes
CREATE TABLE categoryes (category_id INTEGER PRIMARY KEY UNIQUE, category_name TEXT NOT NULL);
INSERT INTO categoryes (category_id, category_name) VALUES (1, 'Обчыные камни');
INSERT INTO categoryes (category_id, category_name) VALUES (2, 'Неплохие камни)');
INSERT INTO categoryes (category_id, category_name) VALUES (3, 'Огого каменюги');
INSERT INTO categoryes (category_id, category_name) VALUES (4, 'Родные камни');
INSERT INTO categoryes (category_id, category_name) VALUES (5, 'Камни из-за бугра');

-- Таблица: item-category
CREATE TABLE "item-category" (item_id INTEGER REFERENCES item_list (item_id) NOT NULL, category_id INTEGER NOT NULL REFERENCES categoryes (category_id));
INSERT INTO "item-category" (item_id, category_id) VALUES (1, 1);
INSERT INTO "item-category" (item_id, category_id) VALUES (2, 2);
INSERT INTO "item-category" (item_id, category_id) VALUES (3, 2);
INSERT INTO "item-category" (item_id, category_id) VALUES (4, 3);
INSERT INTO "item-category" (item_id, category_id) VALUES (1, 4);
INSERT INTO "item-category" (item_id, category_id) VALUES (2, 4);
INSERT INTO "item-category" (item_id, category_id) VALUES (3, 4);
INSERT INTO "item-category" (item_id, category_id) VALUES (4, 5);

-- Таблица: item_list
CREATE TABLE item_list (item_id INTEGER PRIMARY KEY UNIQUE NOT NULL, name TEXT NOT NULL, cost DOUBLE NOT NULL, count INTEGER NOT NULL);
INSERT INTO item_list (item_id, name, cost, count) VALUES (1, 'СЕРЫЙ КАМЕНЬ!!', 'НЕДОРОГО НО СЕРДИТО!', 1000000);
INSERT INTO item_list (item_id, name, cost, count) VALUES (2, 'ЭТО ЖЕВЛТЫЙ КАМЕНЬ! КАМЕНЮЮА!!!', 154.0, 777777);
INSERT INTO item_list (item_id, name, cost, count) VALUES (3, 'НЕ МОЖЕТ БЫВТЫЬ! В ЭТОМ КАМНЕ! ДЫРКИМ!И!', 'ВРЕМЯ ДЕНЬГИ', 1000);
INSERT INTO item_list (item_id, name, cost, count) VALUES (4, 'ВЕНЕРА', 'ОТЛИЧНО!', 0);

-- Таблица: shoping_cart
CREATE TABLE shoping_cart (user_id INTEGER REFERENCES users (user_id) NOT NULL, item_id INTEGER REFERENCES item_list (item_id) NOT NULL, count INTEGER NOT NULL);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (1, 4, 1);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 1, 200);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 2, 10);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 3, 2);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (3, 2, 20);

-- Таблица: users
CREATE TABLE users (user_id INTEGER PRIMARY KEY NOT NULL UNIQUE, name TEXT NOT NULL, phone TEXT UNIQUE NOT NULL, email TEXT UNIQUE, registration_date DATE);
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (1, 'Неизвестный пользователь', '+1000-7', NULL, NULL);
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (2, 'Василий Улюлюков', '+1234(777)-1-1', NULL, NULL);
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (3, 'Кириллл Алелехов', '+7(567)-123-213-123123', 'chort@sobaka.dog', NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
