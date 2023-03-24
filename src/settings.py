import os
from dotenv import load_dotenv

load_dotenv()

DB_PSW = os.getenv('DB_PSW')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
