from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

admin = Admin(app)

class Service(db.Model):
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer(), primary_key=True) 
    date = db.Column(db.String(12), nullable=False)
    guest = db.Column(db.Integer(), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    #submit=db.Column(db.SubmitField('submit'))
    
    def __repr__(self) ->str:
        return f"<Service: {self.name}-{self.phone}>"

admin.add_view(ModelView(Service, db.session))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/product/cones")
def cones():
    return render_template('cones.html')

@app.route("/product/scopes")
def scopes():
    return render_template('scopes.html')

@app.route("/product/bars")
def bars():
    return render_template('bars.html')

@app.route("/product/kulfi")
def kulfi():
    return render_template('kulfi.html')

@app.route("/product/family")
def family():
    return render_template('family.html')

@app.route("/product/party")
def party():
    return render_template('party.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/services", methods=['GET','POST'])
def services():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        guest = request.form.get('number')
        date = request.form.get('date')
        address = request.form.get('desc')
        entry = Service(name=name, phone = phone, address = address, date= date,email = email, guest=guest )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("services.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
