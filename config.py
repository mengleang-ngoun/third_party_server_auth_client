import os
from dotenv import load_dotenv

load_dotenv()

EKYC_CLIENT_ID = os.getenv('EKYC_CLIENT_ID')
EKYC_CLIENT_SECRET = os.getenv('EKYC_CLIENT_SECRET')
