from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import add_item, move_item, get_items
from todo_app.view_models.view_model import ViewModel

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config())
    
    @app.route('/add', methods=['POST'])
    def addToDo():
        add_item(request.form.get('new-item'))
        return redirect('/')

    @app.route('/to-do/<id>', methods=['POST'])
    def to_do(id):
        move_item(id, 'To Do')
        return redirect('/')

    @app.route('/doing/<id>', methods=['POST'])
    def doing(id):
        move_item(id, 'Doing')
        return redirect('/')

    @app.route('/complete/<id>', methods=['POST'])
    def complete(id):
        move_item(id, 'Done')
        return redirect('/')

    @app.route('/')
    def index():
        item_view_model = ViewModel(get_items())
        return render_template('index.html', view_model=item_view_model)
    
    return app