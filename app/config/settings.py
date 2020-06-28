import os

from dotenv import load_dotenv, find_dotenv


load_dotenv()

# Third party APIs
RAPID_API_HOST = os.getenv("RAPID_API_HOST")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

REST_COUNTRIES_HOST = os.getenv("REST_COUNTRIES_HOST")

# Database SQLite
DB_FILE = os.getenv("DB_FILE")
