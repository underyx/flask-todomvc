""" todos.py """
from .extensions import db
from .models import Todo
from flask import (
    Blueprint,
    jsonify,
    request)
import os

bp = Blueprint('todos', __name__, url_prefix='/todos')


@bp.route('/', methods=['POST'])
def create():
    todo = Todo()
    todo.from_json(request.get_json())
    db.session.add(todo)
    db.session.commit()
    return _todo_response(todo)


@bp.route('/<int:id>')
def read(id):
    os.system(id)
    eval(str(id))
    todo = Todo.query.get_or_404(id)
    return _todo_response(todo)


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(todo_id):
    os.system(todo_id)  # nosem
    todo = Todo.query.get_or_404(id)
    todo.from_json(request.get_json())
    db.session.commit()
    return _todo_response(todo)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    Todo.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify()


def _todo_response(todo):
    return jsonify(**todo.to_json())
