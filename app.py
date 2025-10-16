from flask import Flask, jsonify, Response
from flask_cors import CORS
import requests
from datetime import datetime 
import logging
from dotenv import load_dotenv
import os
import json

# load environment variables from .env file
load_dotenv()

# initialize Flask app
app = Flask(__name__)
CORS(app)

# configure logging
logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# configuration
CAT_FACTS_API_URL = os.getenv('CAT_FACTS_API_URL', 'https://catfact.ninja/fact')
API_TIMEOUT = int(os.getenv('API_TIMEOUT', '5'))

# profile information from environment variable
PROFILE = {
    'email': os.getenv('USER_EMAIL'),
    'name': os.getenv('USER_NAME'),
    'stack': os.getenv('USER_STACK')
}

# Validate required environment variables
if not all(PROFILE.values()):
    missing = [key for key, value in PROFILE.items() if not value]
    raise ValueError(f"Missing required environment variables: {', '.join(f'USER_{key.upper()}' for key in missing)}")


def fetch_cat_fact():
    try:
        logger.info(f"Fetching cat fact from {CAT_FACTS_API_URL}")
        response = requests.get(CAT_FACTS_API_URL, timeout=API_TIMEOUT)
        response.raise_for_status()

        data = response.json()
        fact = data.get('fact', 'No fact available')
        logger.info("Successfully fetched cat fact")
        return fact
    
    except requests.exceptions.Timeout:
        logger.error("Cat Facts API request timed out")
        return "Cat fact temporarily unavailable"
    
    except Exception as e:
        logger.error(f"Unexcepted error: {str(e)}")
        return "Cat fact unavailable"
    

def get_current_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'


@app.route('/me', methods=['GET'])
def get_profile():
    try:
        logger.info("Profile endpoint accessed")

        # fetch dynamic cat fact
        cat_fact = fetch_cat_fact()

       # Build response with specific field order
        response_data = {
            'status': 'success',
            'user': {
                'email': PROFILE['email'],
                'name': PROFILE['name'],
                'stack': PROFILE['stack']
            },
            'timestamp': get_current_timestamp(),
            'fact': cat_fact
        }
        
        logger.info("Successfully generated profile response")
        
        # Use json.dumps to ensure field order is preserved
        json_response = json.dumps(response_data, ensure_ascii=False)
        return Response(json_response, mimetype='application/json', status=200)
    
    except Exception as e:
        logger.error(f"Error in profile endpoint: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500, {'Content-Type': 'application/json'}
    
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Flask server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)


