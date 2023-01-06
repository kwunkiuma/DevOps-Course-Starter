from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, login_required, login_user, current_user

from todo_app.authentication.login import get_access_token, get_login_url, get_user
from todo_app.authentication.user import User, WRITER
from todo_app.data.db_items import add_item, get_items, move_item
from todo_app.flask_config import Config
from todo_app.view_models.view_model import ViewModel

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route("/add", methods=["POST"])
    @login_required
    def add_to_do():
        add_item(request.form.get("new-item"))
        return redirect("/")

    @app.route("/to-do/<id>", methods=["POST"])
    @login_required
    def to_do(id):
        move_item(id, "To Do")
        return redirect("/")

    @app.route("/doing/<id>", methods=["POST"])
    @login_required
    def doing(id):
        move_item(id, "Doing")
        return redirect("/")

    @app.route("/complete/<id>", methods=["POST"])
    @login_required
    def complete(id):
        move_item(id, "Done")
        return redirect("/")

    @app.route("/login/callback", methods=["get"])
    def login():
        code = request.args["code"]

        access_token = get_access_token(code)
        user = get_user(access_token)
        login_user(user)
        return redirect("/")

    @app.route("/")
    @login_required
    def index():
        if app.config.get("LOGIN_DISABLED"):
            role = WRITER
        else:
            role = current_user.role
        item_view_model = ViewModel(get_items(), role)
        return render_template("index.html", view_model=item_view_model)

    @login_manager.unauthorized_handler
    def unauthenticated():
        return redirect(get_login_url())

    @login_manager.user_loader
    def load_user(user_id):
        user = User(user_id)
        return user

    login_manager.init_app(app)

    return app
