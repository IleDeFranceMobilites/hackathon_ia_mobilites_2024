from directions import DirectionsAPI
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
# Load environment variables
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Configuration
app.config['DEBUG'] = True  # Enable debug mode for development
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

# Initialize DirectionsAPI with API key from environment variable
directions = DirectionsAPI(api_key=os.getenv('DIRECTIONS_API_KEY', 'REMOVED'))

# Enable CORS for all routes
CORS(app)


# Sample route
@app.route('/')
def hello():
    return "Hello, World!"

# Sample API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "This is sample data from the API"}
    return jsonify(data)

# Route for directions
@app.route('/api/directions', methods=['GET'])
def get_directions():
    try:
        # Extract parameters from the request
        origin_long = request.args.get('origin_long')
        origin_lat = request.args.get('origin_lat')
        dest_long = request.args.get('dest_long')
        dest_lat = request.args.get('dest_lat')
        datetime_str = request.args.get('datetime')
        wheelchair = request.args.get('wheelchair', 'false').lower() == 'true'

        # Validate required parameters
        if not all([origin_long, origin_lat, dest_long, dest_lat, datetime_str]):
            return jsonify({"error": "Missing required parameters"}), 400

        # Get journey information
        journey_data = directions.get_journey_info(
            origin_long, origin_lat, dest_long, dest_lat, datetime_str, wheelchair
        )

        if journey_data is None:
            return jsonify({"error": "Failed to fetch journey information"}), 500

        # Parse journey data
        parsed_journeys = directions.parse_journey_data(journey_data)

        return jsonify(parsed_journeys)

    except Exception as e:
        return jsonify({"error": str(e)}), 500






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3100)
