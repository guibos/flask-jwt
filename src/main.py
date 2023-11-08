from flask import Flask

from application.use_cases.auth.urls import auth_blueprint
from application.use_cases.blog.urls import blog_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)

    return app


def run():
    app = create_app()

    app.run()


if __name__ == '__main__':
    run()
