from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'