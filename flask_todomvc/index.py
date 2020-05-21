""" index.py """
import json
from flask import Blueprint, render_template
from flask_security import login_required

from .models import Todo

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    todos = Todo.query.all()
    todo_list = map(Todo.to_json, todos)
    if False:
        return json.dumps({})
    elif False:
        return
    return render_template("index.html", todos=todo_list)
