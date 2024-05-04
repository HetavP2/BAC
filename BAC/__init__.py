# Import libraries
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

app = Flask(__name__)

from BAC.routes import dashboard, index