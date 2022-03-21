from flask import request, render_template, escape, session, redirect, url_for
from orm import *
from init import app


def workers_list_func(lst, n=4):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



@app.route('/main')
@app.route('/')
def main_page():
    return render_template("main.html", news=News.query.all())


@app.route('/catalog')
def catalog():
    return render_template("catalog.html", items=Items.query.all())


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        if Users.query.filter_by(name=session['name']).one().validate(old_password):
            Users.query.filter_by(name=session['name']).one().password = hashlib.md5(new_password.encode('utf8')).hexdigest()
            db.session.commit()
    return render_template("profile.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('name')
        password = request.form.get('password')
        try:
            if Users.query.filter_by(name=username).one().validate(password):
                session['name'] = username
                session['status'] = Users.query.filter_by(name=username).one().status
                return redirect(url_for('main'), code=301)
        except:
            pass

    return render_template('login.html')


@app.route('/cart', methods=['GET', 'POST'])
def cart_page():
    cart = []
    if request.method == 'POST':

        id = request.form.get('id')
        try:
            Cart_record.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            print('Error cart_page')
    for i in Users.query.filter_by(name=session['name']).one().cart:
        cart.append((Items.query.filter_by(id=i.item_id).one(), i))
    return render_template('cart.html', cart=cart)


@app.route('/about')
def about():
    workers = Workers.query.all()
    workers_list = workers_list_func(workers)
    return render_template("about.html", workers_list=workers_list)


def add_to_cart(item_id, user_id, count):
    if count <= 0:
        return
    try:
        Record = Cart_record.query.filter_by(user_id=user_id, item_id=item_id).one()
        Record.count += count
    except:
        record = Cart_record(item_id=item_id, user_id=user_id, count=count)
        db.session.add(record)
    db.session.commit()


@app.route('/item/<item_id>', methods=['GET', 'POST'])
def show_item(item_id):
    item_id = escape(item_id)

    if request.method == 'POST':
        print(request.form.get('type'))
        if request.form.get('type') == "buy":
            count = int(request.form.get('count'))
            add_to_cart(item_id, Users.query.filter_by(name=session['name']).one().id, count)

        elif request.form.get('type') == "minus_cat":
            Items.query.first().categories.remove(Categories.query.filter_by(id=int(request.form.get('id'))).one())
            db.session.commit()
        else:
            cat = Categories.query.filter_by(id=int(request.form.get('id'))).one()
            item = Items.query.filter_by(id=item_id).one()
            if not cat in item.categories:
                item.categories.append(cat)
            db.session.commit()
    return render_template("item.html", item=Items.query.filter_by(id=item_id).one(), categories=Items.query.filter_by(id=item_id).one().categories, all_categories=Categories.query.all())


@app.route('/logout')
def logout():
    if session.get('name'):
        session.pop('name')
        session.pop('status')
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run(debug=True)
