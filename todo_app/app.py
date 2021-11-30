from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import add_item, get_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/add', methods=['POST'])
def submitFilm():
    add_item(request.form.get('title'))
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html', items=get_items())
