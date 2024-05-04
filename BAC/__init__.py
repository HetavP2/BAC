# Import libraries
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
# bucket_id = 'https://mwhsfjnxtnwgycvxqxbb.supabase.co/storage/v1/s3'
# supabase.storage().create_bucket(bucket_id, public=True)

app = Flask(__name__)

from BAC.routes import dashboard, index