# Import libraries
from flask import render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from BAC.flaskforms import LoginForm

# Import custom libraries
from BAC import app, supabase


@app.route('/dashboard', methods=['GET', "POST"])
def dashboard():
    data=supabase.table("people").select("*").execute()
    print(data)
    # userArts = getArt(current_user.id)

    data2 = supabase.table("people").insert({"user_name": "Hetav", "points": 900}).execute()

    return render_template('dashboard.html') 

@app.route('/login', methods=['GET'])
def login():
    user = supabase.auth.sign_up(email="hetav.j.patel@gmail.com", password="123")
    form = LoginForm()
    # userArts = getArt(current_user.id)

    return render_template('login.html', form=form) 
