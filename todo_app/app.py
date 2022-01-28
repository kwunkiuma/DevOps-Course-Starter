from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import add_item, complete_item, get_items
from todo_app.view_models.view_model import ViewModel

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
    item_view_model = ViewModel(get_items())
    return render_template('index.html', view_model=item_view_model)
