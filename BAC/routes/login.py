# Import libraries
from flask import render_template, redirect, url_for, flash

# Import custom libraries
from BAC import app

@app.route('/login', methods=['GET'])
def login():
    # userArts = getArt(current_user.id)

    return render_template('login.html') 
