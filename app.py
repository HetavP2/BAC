from BAC import app

# @app.route("/", methods=['GET'])
# def arts():
#     return str('alexcreate the grid')
app.config['SECRET_KEY'] = 'wolfhacksstuff'



if __name__ == "__main__":
    app.run(debug=True)

    
    
