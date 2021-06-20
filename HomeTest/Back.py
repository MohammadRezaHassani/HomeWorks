from flask import Flask, request, render_template
app = Flask(__name__, template_folder='Templates')


class Staff:
    id = 0
    user_dict = {}

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def register(cls, first_name, last_name):
        user = cls(first_name, last_name)
        Staff.user_dict[Staff.id] = user
        Staff.id += 1


@app.route('/', methods=['GET'])
def show_form():
    return render_template('reg.html')


@app.route('/', methods=['post'])
def reg_user():
    print(request.form['firstName'])


# return render_template('reg.html')


app.run()
