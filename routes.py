from flask import Blueprint, jsonify, request
from extensions import db  # Import db from extensions, not app.py
from models import Destination  # Import Destination model from models.py

api = Blueprint('api', __name__)

@api.route("/")
def home():
    return jsonify({"message": "Welcome to GlobeTrekker API!"})

@api.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])

@api.route("/destinations", methods=["POST"])
def add_destination():
    data = request.get_json()
    
    # Safely get the data, or use a default value
    destination = data.get("destination")
    country = data.get("country")
    rating = data.get("rating")

    # Ensure all required fields are provided
    if not destination or not country or not rating:
        return jsonify({"error": "Missing required fields"}), 400

    new_destination = Destination(
        destination=destination,
        country=country,
        rating=rating
    )
    
    db.session.add(new_destination)
    db.session.commit()
    
    return jsonify(new_destination.to_dict()), 201
