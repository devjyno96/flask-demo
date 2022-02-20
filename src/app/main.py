from flask import Flask


def create_app():
    app = Flask(__name__)

    from src.app.router import item
    app.register_blueprint(item.bp)

    return app


app = create_app()


@app.route('/')
def test():
    return 'test'


if __name__ == "__main__":
    app.run()
