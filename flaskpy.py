from flask import Flask, request, render_template, escape
from orm import *
from init import app


@app.route('/')
def main_page():
    return render_template("main.html", news=News.query.all())


@app.route('/catalog')
def catalog():
    return render_template("catalog.html", items=Items.query.all())


@app.route('/about')
def about():
    workers_list = []
    workers = Workers.query.all()
    k = 0
    tmp = []
    for i in workers:
        tmp.append(i)
        k += 1
        if k == 4:
            workers_list.append(tmp)
            tmp = []
            k = 0
    if tmp:
        workers_list.append(tmp)
    print(workers_list)
    return render_template("about.html", workers_list=workers_list)


@app.route('/item/<item_id>')
def show_item(item_id):
    item_id = escape(item_id)
    return render_template("item.html", item=Items.query.filter_by(id=item_id).one())


if __name__ == '__main__':
    app.run(debug=True)
