from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


def menu():
    return render_template('menu.html')


app.add_url_rule("/menu", 'menu', menu)

app.run()
