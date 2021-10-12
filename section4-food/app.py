from flask import Flask, render_template, request
import db_connect as db

app = Flask(__name__)
# app.debug = True


@app.teardown_appcontext
def close_database(error):
    db.close_db(error)


@app.route('/')
def index() -> str:
    return render_template('home.html')


@app.route('/view')
def view():
    return render_template('day.html')


@app.route('/food', methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        print('post')
        return 'submitted'
    return render_template('add_food.html')


if __name__ == '__main__':
    app.run()
