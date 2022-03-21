import hashlib
from datetime import datetime
from init import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(80), unique=True)
    reg_date = db.Column(db.DateTime)
    b_date = db.Column(db.DateTime)
    password = db.Column(db.String(256), unique=True, nullable=False)
    status = db.Column(db.String(80), unique=True)
    cart = db.relationship('Cart_record')

    def validate(self, password):
        return self.password == hashlib.md5(password.encode('utf8')).hexdigest()


Item_Categories = db.Table(
    'item_categories',
    db.Column('item_id', db.Integer(), db.ForeignKey('items.id')),
    db.Column('c_id', db.Integer(), db.ForeignKey('categories.id'))
)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'[{self.id}] {self.name}'


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Integer)
    count = db.Column(db.Integer)
    image = db.Column(db.String(80))
    desc = db.Column(db.String(200))
    color = db.Column(db.String(80))
    mass = db.Column(db.String(80))
    taste = db.Column(db.String(80))
    cost_text = db.Column(db.String(80))
    categories = db.relationship('Categories', secondary=Item_Categories, backref=db.backref('Items', lazy=False))

    def __repr__(self):
        return f'[{self.id}] {self.name}'


class Cart_record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    count = db.Column(db.Integer)


class Workers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(80))


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(40))


db.create_all()

'''db.session.add(Categories(name="Обчыные камни"))
db.session.add(Categories(name="Неплохие камни"))
db.session.add(Categories(name="Огого каменюги"))
db.session.add(Categories(name="Родные камни"))
db.session.add(Categories(name="Камни из-за бугра"))'''

'''a = [(1, 'СЕРЫЙ КАМЕНЬ!!', 15.0, 1000000),
     (2, 'ЭТО ЖЕВЛТЫЙ КАМЕНЬ! КАМЕНЮЮА!!!', 154.0, 777777),
     (3, 'НЕ МОЖЕТ БЫВТЫЬ! В ЭТОМ КАМНЕ! ДЫРКИМ!И!', 1000.0, 1000),
     (4, 'ВЕНЕРА', 1000000000099.0, 0)
     ]
for i in a:
    x = Items(name=i[1], cost=i[2], count=i[3])
    db.session.add(x)'''

'''x = Items.query.all()
for i in x:
    print(i.name)'''
'''x = Items(name='Тест', cost=-100, count=1)
c1 = Categories.query.all()[0]
x.categories.append(c1)
print(x.categories)'''

if __name__ == '__main__':
    pass

db.session.commit()

'''
CREATE TABLE categoryes (category_id INTEGER PRIMARY KEY UNIQUE, category_name TEXT NOT NULL);
INSERT INTO categoryes (category_id, category_name) VALUES (1, 'Обчыные камни');
INSERT INTO categoryes (category_id, category_name) VALUES (2, 'Неплохие камни)');
INSERT INTO categoryes (category_id, category_name) VALUES (3, 'Огого каменюги');
INSERT INTO categoryes (category_id, category_name) VALUES (4, 'Родные камни');
INSERT INTO categoryes (category_id, category_name) VALUES (5, 'Камни из-за бугра');

-- Таблица: item_category
CREATE TABLE item_category (item_id INTEGER REFERENCES item_list (item_id) NOT NULL, category_id INTEGER NOT NULL REFERENCES categoryes (category_id));
INSERT INTO item_category (item_id, category_id) VALUES (1, 1);
INSERT INTO item_category (item_id, category_id) VALUES (2, 2);
INSERT INTO item_category (item_id, category_id) VALUES (3, 2);
INSERT INTO item_category (item_id, category_id) VALUES (4, 3);
INSERT INTO item_category (item_id, category_id) VALUES (1, 4);
INSERT INTO item_category (item_id, category_id) VALUES (2, 4);
INSERT INTO item_category (item_id, category_id) VALUES (3, 4);
INSERT INTO item_category (item_id, category_id) VALUES (4, 5);

-- Таблица: item_list
CREATE TABLE item_list (item_id INTEGER PRIMARY KEY UNIQUE NOT NULL, name TEXT NOT NULL, cost DOUBLE NOT NULL, count INTEGER NOT NULL);
INSERT INTO item_list (item_id, name, cost, count) VALUES (1, 'СЕРЫЙ КАМЕНЬ!!', 15.0, 1000000);
INSERT INTO item_list (item_id, name, cost, count) VALUES (2, 'ЭТО ЖЕВЛТЫЙ КАМЕНЬ! КАМЕНЮЮА!!!', 154.0, 777777);
INSERT INTO item_list (item_id, name, cost, count) VALUES (3, 'НЕ МОЖЕТ БЫВТЫЬ! В ЭТОМ КАМНЕ! ДЫРКИМ!И!', 1000.0, 1000);
INSERT INTO item_list (item_id, name, cost, count) VALUES (4, 'ВЕНЕРА', 1000000000099.0, 0);

-- Таблица: shoping_cart
CREATE TABLE shoping_cart (user_id INTEGER REFERENCES users (user_id) NOT NULL, item_id INTEGER REFERENCES item_list (item_id) NOT NULL, count INTEGER NOT NULL);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (1, 4, 1);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 1, 200);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 2, 10);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (2, 3, 2);
INSERT INTO shoping_cart (user_id, item_id, count) VALUES (3, 2, 20);

-- Таблица: users
CREATE TABLE users (user_id INTEGER PRIMARY KEY NOT NULL UNIQUE, name TEXT NOT NULL, phone TEXT UNIQUE NOT NULL, email TEXT UNIQUE, registration_date DATE);
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (1, 'Неизвестный пользователь', '+1000-7', NULL, '12-04-2008');
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (2, 'Василий Улюлюков', '+1234(777)-1-1', NULL, '04-12-2019');
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (3, 'Кириллл Алелехов', '+7(567)-123-213-123123', 'chort@sobaka.dog', '10-05-2018');
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (4, 'Алесандр Девяточкин', '891262351923', NULL, '30-08-2020');
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (5, 'Наверно Лучший Человек В Мире', '+7(916)-565-61-20', 'andrey.12.56.34@gmail.com', '23-11-2021');
INSERT INTO users (user_id, name, phone, email, registration_date) VALUES (6, 'Пророк Мухамед', '89121234567', NULL, '05-01-2019');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
'''
