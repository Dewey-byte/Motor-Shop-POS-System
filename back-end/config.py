import os

# Base directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Create 'data' directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR, exist_ok=True)

# Database configuration
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(DATA_DIR, 'motos_pos.db'))
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-secret')

# Flask-Session settings
SESSION_TYPE = 'filesystem'
SESSION_FILE_DIR = os.path.join(DATA_DIR, 'flask_sessions')

# Create session directory if it doesn't exist
if not os.path.exists(SESSION_FILE_DIR):
    os.makedirs(SESSION_FILE_DIR, exist_ok=True)
