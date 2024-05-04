# Import libraries
from flask import render_template,request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from BAC.flaskforms import LoginForm, ArtForm
from werkzeug.utils import secure_filename
from BAC.models import Arts
# Import custom libraries
from BAC import app, supabase, db



global logged
global user_info
logged = False

@app.route('/dashboard', methods=['GET', "POST"])
def dashboard():
    global logged, user_info
    # user_id = user_info['user_id']
    # print(user_id)
    form = ArtForm()

    if logged == True:
        print(True)
        print(user_info)
    else:
        print(False)
    # userArts = getArt(current_user.id)

    # data2 = supabase.table("people").insert({"user_name": "Hetav", "points": 900}).execute()

    return render_template('dashboard.html', form=form) 

@app.route('/submitart', methods=['GET', "POST"])
def submitart():
    global user_info

    # userArts = getArt(current_user.id)
    # form = ArtForm()
    if request.method == 'POST':
        
        file_name = request.form['file_name']
        message = request.form['message']
        file_upload = request.files['fileupload']
        filename = secure_filename(file_upload.filename)
        # mimetype = file_upload.mimetype
        # uploading = Arts(filename=filename, data=file_upload.read())
        # db.session.add(uploading)
        # db.session.commit()
        # print(type(uploading))
        # uploadFile = supabase.storage.from_("arts").upload(filename, file_upload)
        # submitartdata = supabase.table("arts").insert({"message": str(message), "file_name":file_name, "user_id": str(user_info.data[0]['user_id']), "user_name": str(user_info.data[0]['user_name'])}).execute()

        # print(uploadFile)
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html') 

@app.route('/arts/<string:artId>', methods=['GET'])
def art_page(artId = ''):
    # global user_info
    # abc = supabase.table("people").update({"points": 100}).eq("user_name", str(user_info.data[0]['user_name'])).execute()
    img = supabase.storage.from_("arts").get_public_url(artId)


    return render_template("art.html", img=img)

@app.route('/purchase/<string:artId>', methods=['POST'])
def purchase(artId = ''):
    # data = supabase.table('arts').update({}).eq().execute()
    return redirect(url_for('dashboard'))


@app.route('/login', methods=["GET",'POST'])
def login():
    global logged, user_info

    form = LoginForm()
    if request.method == 'POST':
        username = request.form['user_name']
        user_info=supabase.table("people").select("*").eq("user_name", username).execute()
        
        logged = True

        return redirect(url_for('dashboard'))
    # userArts = getArt(current_user.id)

    return render_template('login.html', form=form) 
