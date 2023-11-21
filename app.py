from flask import Flask , render_template,request,url_for,redirect
import random
import sqlite3


app = Flask(__name__)
app.secret_key = 'jkxnkvbx!m knnkdbvl:xl, XBBs'
upload_folder = "static/assets/img/"
allowed_exta= ["jpg","png","jpeg","svg"]
app.config["UPLOAD_FOLDER"] = upload_folder

conn = sqlite3.connect("static/assets/database.db",check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def allowed_file(image):
    extansion = image.filename.split(".")[-1].lower()
    if "." in image.filename and extansion in allowed_exta:
        filename = (f'aa_{random.randint(1,1000)}{random.randint(1000,10000)}_community_image.{extansion}')
        image.save(f'{app.config["UPLOAD_FOLDER"]}{filename}')
        return f'{app.config["UPLOAD_FOLDER"]}{filename}'
    else:
        return f'{app.config["UPLOAD_FOLDER"]}{"1.jpg"}'


@app.route('/')
def home():
    result= cursor.execute("select * from users")
    datas= [dict(d) for d in result.fetchall()]
    return render_template("index.html",datas = datas ,isEmpty = len(datas))

@app.route('/add' , methods = ["POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        tag = request.form.get("tag")
        about = request.form.get("about")
        if "image" in request.files:
            image = request.files.get("image")
            filename = allowed_file(image)
        else:
            filename = f'{app.config["UPLOAD_FOLDER"]}{"1.jpg"}'
        linkedin = request.form.get("linkedin")
        website = request.form.get("website")
        github = request.form.get("github")
        youtube = request.form.get("youtube")
        whatsapp = request.form.get("whatsapp")
        x = request.form.get("x")
        facebook = request.form.get("facebook")
        telegram = request.form.get("telegram")

        datas = (filename,name,about,linkedin,whatsapp,youtube,github,website,facebook,x,telegram,tag)
        req = '''INSERT INTO  "users" ("image", "name", "about", "linkedin", "whatsapp", "youtube", "github", "web", "facebook", "x", "telegram","tag" ) 
        VALUES (?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?,?)'''

        cursor.execute(req,datas)
        conn.commit()
        return redirect(url_for('addone'))

@app.route('/search' , methods = ["POST"])
def search():
    qery = request.form.get("search")
    if qery == '':
        result= cursor.execute("select * from users")
        datas= [dict(d) for d in result.fetchall()]
        return render_template('index.html',datas = datas ,isEmpty = len(datas))
    result = cursor.execute("SELECT * FROM users WHERE name LIKE ? OR about LIKE ?",('%'+qery+'%' , '%'+qery+'%'))
    datas = [dict(data) for data in result.fetchall()]
    return render_template('index.html',datas = datas,isEmpty = len(datas))


@app.route('/addone')
def addone():
    result= cursor.execute("select * from users")
    datas= [dict(d) for d in result.fetchall()]
    return render_template("compo.html",datas = datas)

if __name__== '__main__':
    app.run(debug=True)
