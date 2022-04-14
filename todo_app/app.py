from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import add_item, complete_item, get_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/add', methods=['POST'])
def addToDo():
    add_item(request.form.get('new-item'))
    return redirect('/')

@app.route('/complete/<id>', methods=['POST'])
def complete(id):
    complete_item(id)
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html', items=get_items())
