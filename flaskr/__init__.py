import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app to be returned
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # otherwise, load the test config if it's passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path) # creates a directory if one doesn't exist
    except OSError:
        pass # otherwise we just move along

    # a simple page that just says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'


    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
