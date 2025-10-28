import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

# You'll need to import your api routes here
#   these are your blueprints.
from .routes.tasks_api import tasks_bp

# This will load from .flaskenv in development
#   and will not be used in deployment. You'll
#   use Sever environment variables to keep them
#   away from prying eyes (you don't put secrets
#   in a web accessible directory).
load_dotenv()

# The create_app function is mostly the same, but we
#   will have some pytest specific setup, so we have
#   a little boolean to help us decide what to setup
#   here or let pytest handle.
def create_app(testing=False):
    
    # The instance_relative stuff basically means
    #   we will plan to have 
    app = Flask(__name__, instance_relative_config=True)

    # This will help us if we have requests to our app that
    # do not originate from the same origin.
    CORS(app)

    # We'll setup all the config stuff at once.
    #   the os.environ.get will pull from .flaskenv
    #   first, and Server environment variables second
    #   so we don't need to change this for deployment.
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(
            app.instance_path,
            # This will establish the database name and provide a
            #   fallback name 'app.sqlite'
            os.environ.get('DATABASE', 'app.sqlite')),
        # We won't use this as it increases overhead on the database
        #   and throws a bunch of warnings.
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # This creates the folder where our data for the app will be
    #   stored. For us, this is just the database.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Don't init SQLAlchemy here if testing, we'll use different settings
    #   in pytest.
    if not testing:
        db.init_app(app)

    # Register the API blueprints
    app.register_blueprint(tasks_bp)

    # Define where our REACT front end is located (primarily for deployment)
    #   No need to change.
    REACT_BUILD_DIR = os.path.join(app.root_path, 'static', 'dist')

    # This is our "catch all" route to server the react app.
    #   Flask is only an API, but when we ask to see content,
    #   it will route us the the React front end which will handle
    #   choosing the right views to show.
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react_app(path):
        file_path = os.path.join(REACT_BUILD_DIR, path)

        if os.path.exists(file_path) and not os.path.isdir(file_path):
            return send_from_directory(REACT_BUILD_DIR, path)
        else:
            return send_from_directory(REACT_BUILD_DIR, 'index.html')

    # This is our handy-dandy flask function to have SQLAlchemy
    #   initialize the database and tables (schema).
    @app.cli.command("initdb")
    def init_database():
        with app.app_context():
            try:
                db.drop_all()
                db.create_all()
                print("Initialized the database.")
            except Exception as e:
                print(f"Error: {e}")

    return app