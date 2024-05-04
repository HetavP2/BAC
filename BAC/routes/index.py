# Import libraries
from flask import render_template, redirect, url_for, flash

# Import custom libraries
from BAC import app

@app.route('/index', methods=['GET'])
def index():
    # userArts = getArt(current_user.id)

    return render_template('index.html') 
