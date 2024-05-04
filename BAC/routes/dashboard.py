# Import libraries
from flask import render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

# Import custom libraries
from BAC import app, supabase


# class UploadArtForm(FlaskForm)

@app.route('/dashboard', methods=['GET', "POST"])
def dashboard():
    data=supabase.table("people").select("*").execute()
    print(data)
    # userArts = getArt(current_user.id)

    data2 = supabase.table("people").insert({"user_name": "Hetav", "points": 900}).execute()

    return render_template('dashboard.html') 
