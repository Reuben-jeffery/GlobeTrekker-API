# sample_data.py
from models import Destination
from extensions import db

def preload_data():
    # Check if any data exists, to avoid adding duplicates
    if Destination.query.count() == 0:
        sample_destinations = [
            Destination(destination="Eiffel Tower", country="France", rating=4.8),
            Destination(destination="Great Wall of China", country="China", rating=4.7),
            Destination(destination="Taj Mahal", country="India", rating=4.9)
        ]
        db.session.add_all(sample_destinations)
        db.session.commit()
