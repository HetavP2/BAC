# Import libraries
from flask import render_template, redirect, url_for, flash

# Import custom libraries
from BAC import app, supabase

gallery = supabase.storage.from_("arts").list()

@app.route('/', methods=['GET'])
def index():
    print(gallery)
    # res = supabase.storage.create_bucket('testing')
    # userArts = getArt(current_user.id)
    return render_template('index.html') 
