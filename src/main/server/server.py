from flask import Flask
from flask_cors import CORS
from src.models.settings.sqlite.connection import db_connection_handler
from src.main.routes.health_routes import health_routes_bp
from src.main.routes.people_routes import people_routes_bp

db_connection_handler.connection_to_db()

app = Flask(__name__)

CORS(app)


app.register_blueprint(health_routes_bp)
app.register_blueprint(people_routes_bp)