import os

import requests
from flask import abort
from flask_login import current_user

from todo_app.authentication.user import User, WRITER


def requires_writer(function):
    def run_if_writer(*args, **kwargs):
        if os.getenv("LOGIN_DISABLED") == "True" or current_user.role == WRITER:
            function(*args, **kwargs)
        else:
            abort(403)

    return run_if_writer


def get_login_url():
    return "https://github.com/login/oauth/authorize?client_id=" + os.environ.get("GITHUB_OAUTH_CLIENT_ID")


def get_access_token(code):
    url = "https://github.com/login/oauth/access_token"

    headers = {"Accept": "application/json"}

    params = {
        "client_id": os.environ.get("GITHUB_OAUTH_CLIENT_ID"),
        "client_secret": os.environ.get("GITHUB_OAUTH_CLIENT_SECRET"),
        "code": code,
        "redirect_uri": os.environ.get("GITHUB_OAUTH_REDIRECT_URI"),
    }

    response = requests.post(url, headers=headers, params=params)
    return response.json()["access_token"]


def get_user(access_token):
    url = "https://api.github.com/user"

    auth = "Bearer " + access_token

    headers = {"Accept": "application/json", "Authorization": auth}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        id = response.json()["id"]
        return User(response.json()["id"])
    else:
        return False
