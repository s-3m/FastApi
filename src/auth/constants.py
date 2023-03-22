import os

from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
TKN_SECRET = os.environ.get('TOKEN_SECRET')

