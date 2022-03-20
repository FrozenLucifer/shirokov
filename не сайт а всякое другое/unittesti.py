import unittest
import sqlite3


class TestBD(unittest.TestCase):
    #В начале
    @classmethod
    def setUpClass(self):
        self.database = sqlite3.connect('test1.db')
        self.cur = self.database.cursor()
        self.cur.execute("CREATE TABLE categoryes (category_id INTEGER PRIMARY KEY UNIQUE, category_name TEXT NOT NULL);")
        self.cur.execute("INSERT INTO categoryes (category_id, category_name) VALUES (1, 'Обчыные камни');")
        self.cur.execute("INSERT INTO categoryes (category_id, category_name) VALUES (2, 'Неплохие камни)');")
        self.cur.execute("INSERT INTO categoryes (category_id, category_name) VALUES (3, 'Огого каменюги');")
        self.cur.execute("INSERT INTO categoryes (category_id, category_name) VALUES (4, 'Родные камни');")
        self.cur.execute("INSERT INTO categoryes (category_id, category_name) VALUES (5, 'Камни из-за бугра');")

        self.cur.execute("CREATE TABLE item_category (item_id INTEGER REFERENCES item_list (item_id) NOT NULL, category_id INTEGER NOT NULL REFERENCES categoryes (category_id));")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (1, 1);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (2, 2);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (3, 2);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (4, 3);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (1, 4);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (2, 4);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (3, 4);")
        self.cur.execute("INSERT INTO item_category (item_id, category_id) VALUES (4, 5);")

        self.cur.execute("CREATE TABLE item_list (item_id INTEGER PRIMARY KEY UNIQUE NOT NULL, name TEXT NOT NULL, cost DOUBLE NOT NULL, count INTEGER NOT NULL);")
        self.cur.execute("INSERT INTO item_list (item_id, name, cost, count) VALUES (1, 'СЕРЫЙ КАМЕНЬ!!', 15.0, 1000000);")
        self.cur.execute("INSERT INTO item_list (item_id, name, cost, count) VALUES (2, 'ЭТО ЖЕВЛТЫЙ КАМЕНЬ! КАМЕНЮЮА!!!', 154.0, 777777);")
        self.cur.execute("INSERT INTO item_list (item_id, name, cost, count) VALUES (3, 'НЕ МОЖЕТ БЫВТЫЬ! В ЭТОМ КАМНЕ! ДЫРКИМ!И!', 1000.0, 1000);")
        self.cur.execute("INSERT INTO item_list (item_id, name, cost, count) VALUES (4, 'ВЕНЕРА', 1000000000099.0, 0);")

        self.cur.execute("CREATE TABLE shoping_cart (user_id INTEGER REFERENCES users (user_id) NOT NULL, item_id INTEGER REFERENCES item_list (item_id) NOT NULL, count INTEGER NOT NULL);")
        self.cur.execute("INSERT INTO shoping_cart (user_id, item_id, count) VALUES (1, 4, 1);")
        self.cur.execute("INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 1, 200);")
        self.cur.execute("INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 2, 10);")
        self.cur.execute("INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 3, 2);")
        self.cur.execute("INSERT INTO shoping_cart (user_id, item_id, count) VALUES (3, 2, 20);")

        self.cur.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY NOT NULL UNIQUE, name TEXT NOT NULL, phone TEXT UNIQUE NOT NULL, email TEXT UNIQUE, registration_date DATE);")
        self.cur.execute("INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (1, 'Неизвестный пользователь', '+1000-7', NULL, '12-04-2008');")
        self.cur.execute("INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (2, 'Василий Улюлюков', '+1234(777)-1-1', NULL, '04-12-2019');")
        self.cur.execute("INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (3, 'Кириллл Алелехов', '+7(567)-123-213-123123', 'chort@sobaka.dog', '10-05-2018');")
        self.cur.execute("INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (4, 'Алесандр Девяточкин', '891262351923', NULL, '30-08-2020');")
        self.cur.execute("INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (5, 'Наверно Лучший Человек В Мире', '+7(916)-565-61-20', 'andrey.12.56.34@gmail.com', '23-11-2021');")
        self.cur.execute("INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (6, 'Пророк Мухамед', '89121234567', NULL, '05-01-2019');")

    # перед каждым тестом
    @classmethod
    def tearDownClass(self):
        self.cur.execute("DROP TABLE categoryes")
        self.cur.execute("DROP TABLE item_category")
        self.cur.execute("DROP TABLE item_list")
        self.cur.execute("DROP TABLE shoping_cart")
        self.cur.execute("DROP TABLE users")
        self.database.commit()

    # тест 1 (корзина по телефону)
    def test_1(self):
        print('Первый тест:')
        self.cur.execute('select * from shoping_cart where user_id = (select user_id from users where phone = "+1234(777)-1-1")')
        print(*self.cur.fetchall())

    # тест 2 (категории по id)
    def test_2(self):
        print('Второй тест:')
        self.cur.execute('select DISTINCT category_id from item_category JOIN shoping_cart where item_category.item_id = shoping_cart.item_id and shoping_cart.user_id=1')
        for el in self.cur.fetchall():
            print(*el)

    def test_3(self):
        print('Третий тест:')
        self.cur.execute('select users.user_id, name from users Join shoping_cart ON users.user_id = shoping_cart.user_id where shoping_cart.item_id = (select item_id from item_category where item_category.category_id = 1)')
        for el in self.cur.fetchall():
            print(*el)



if __name__ == "__main__":
    unittest.main()
