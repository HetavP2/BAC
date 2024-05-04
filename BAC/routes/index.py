# Import libraries
from flask import render_template, redirect, url_for, flash

# Import custom libraries
from BAC import app, supabase

gallery = supabase.storage.from_("arts").list()
# https://mwhsfjnxtnwgycvxqxbb.supabase.co/storage/v1/object/public/arts/logo.png
# https://mwhsfjnxtnwgycvxqxbb.supabase.co/storage/v1/object/public/arts/side%20picture.png
@app.route('/', methods=['GET'])
def index():
    listofImgs = []
    count = 0
    for img in gallery:
        listofImgs.append(("https://mwhsfjnxtnwgycvxqxbb.supabase.co/storage/v1/object/public/arts/"+img['name'], img['name']))
        count = count + 1

    # userArts = getArt(current_user.id)
    print(listofImgs)
    return render_template('index.html', listofImgs=listofImgs) 
