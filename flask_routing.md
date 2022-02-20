# Flask Routing

라우트를 분리하려면 뭘 써야 하는가? - Blue Print

```python
# item.py
from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'
```

```python
# main.py
from flask import Flask


def create_app():
    app = Flask(__name__)

    from src.app.router import item
    app.register_blueprint(item.bp)  # 여기서 item.py 의 blue print router를 넣어줌

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

```

