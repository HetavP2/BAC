# Import libraries
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

import os
from supabase import create_client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wolfhackssecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.mwhsfjnxtnwgycvxqxbb:2yTaG9nWBHs4gnN1@aws-0-ca-central-1.pooler.supabase.com:5432/postgres'
db = SQLAlchemy(app)
# bucket_id = 'abc23'
# supabase.storage.create_bucket(bucket_id)
from BAC.routes import dashboard, index