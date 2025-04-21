from flask import Flask
from extensions import db  # Importing db from extensions
from routes import api  # Blueprint import from routes
from sample_data import preload_data  # Preload data import

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable track modifications warning

    # Initialize db with Flask app
    db.init_app(app)

    # Register blueprint for API routes
    app.register_blueprint(api)

    # Setup database tables and preload sample data within app context
    with app.app_context():
        db.create_all()  # Create all tables
        preload_data()   # Preload sample data into the database

    return app

# If running directly, start the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
