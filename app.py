from flask import Flask, render_template
import os
import uuid
from flask import Flask, session,render_template,request, Response, redirect, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from db import db_init, db
from models import  User, Product
from datetime import datetime
#from flask_session import Session
from helpers import login_required
#import razorpay

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

#static file path
@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

#signup as merchant
@app.route("/signup1", methods=["GET","POST"])
def signup2():
	if request.method=="POST":
		session.clear()
		password = request.form.get("password")
		repassword = request.form.get("repassword")
		if(password!=repassword):
			return render_template("error.html", message="Passwords do not match!")

		#hash password
		pw_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
		
		fullname = request.form.get("fullname")
		username = request.form.get("username")
		#store in database
		new_user =User(fullname=fullname,username=username,password=pw_hash)
		try:
			db.session.add(new_user)
			db.session.commit()
		except:
			return render_template("error.html", message="Username already exists!")
		return render_template("login1.html", msg="Account created!")
	return render_template("signup1.html")

#login as merchant
@app.route("/login1", methods=["GET", "POST"])
def login():
	if request.method=="POST":
		session.clear()
		username = request.form.get("username")
		password = request.form.get("password")
		result = User.query.filter_by(username=username).first()
		print(result)
		# Ensure username exists and password is correct
		if result == None or not check_password_hash(result.password, password):
			return render_template("error.html", message="Invalid username and/or password")
		# Remember which user has logged in
		session["username"] = result.username
		return redirect("/home")
	return render_template("login1.html")

#logout
@app.route("/logout")
def logout():
	session.clear()
	return redirect("/login1")

#view all products
@app.route("/")
def index():
	rows = Product.query.all()
	return render_template("index1.html", rows=rows)

#merchant home page to add new products and edit existing products
@app.route("/home", methods=["GET", "POST"], endpoint='home')
@login_required
def home2():
	if request.method == "POST":
		image = request.files['image']
		filename = str(uuid.uuid1())+os.path.splitext(image.filename)[1]
		image.save(os.path.join("static/images", filename))
		category= request.form.get("category")
		name = request.form.get("pro_name")
		description = request.form.get("description")
		price_range = request.form.get("price_range")
		comments = request.form.get("comments")
		new_pro = Product(category=category,name=name,description=description,price_range=price_range,comments=comments, filename=filename, username=session['username'])
		db.session.add(new_pro)
		db.session.commit()
		rows = Product.query.filter_by(username=session['username'])
		return render_template("home.html", rows=rows, message="Product added")
	
	rows = Product.query.filter_by(username=session['username'])
	return render_template("home.html", rows=rows)

#when edit product option is selected this function is loaded
@app.route("/edit/<int:pro_id>", methods=["GET", "POST"], endpoint='edit')
@login_required
def edit1(pro_id):
	#select only the editing product from db
	result = Product.query.filter_by(pro_id = pro_id).first()
	if request.method == "POST":
		#throw error when some merchant tries to edit product of other merchant
		if result.username != session['username']:
			return render_template("error.html", message="You are not authorized to edit this product")
		category= request.form.get("category")
		name = request.form.get("pro_name")
		description = request.form.get("description")
		price_range = request.form.get("price_range")
		comments = request.form.get("comments")
		result.category = category
		result.name = name
		result.description = description
		result.comments = comments
		result.price_range = price_range
		db.session.commit()
		rows = Product.query.filter_by(username=session['username'])
		return render_template("home.html", rows=rows, message="Product edited")
	return render_template("edit.html", result=result)


app = Flask(__name__)


@app.route('/') 
def main():  
    return render_template('3Dnavbar.html')





@app.route('/3Dnavbar.html') 
def home():  
    return render_template('3Dnavbar.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html')
def signin():
    return render_template('login.html')

@app.route('/index1.html')
def index1():
     return render_template('index1.html')


@app.route('/login.php')
def signin_():
    return render_template('login.php')



@app.route('/login1.html')
def login1():
     return render_template('login1.html')



@app.route('/error.html')
def error():
     return render_template('error.html')

@app.route('/edit.html')
def edit():
     return render_template('edit.html')



@app.route('/signup2.html')
def signup1():
     return render_template('signup1.html')

@app.route('/signup.html')
def signup():
     return render_template('signup1.html')


@app.route('/home.html')
def home1():
     return render_template('home.html')

@app.route('/layout.html')
def layout():
     return render_template('layout.html')


@app.route('/signup-check.php')
def signupcheck():
    return render_template('signup-check.php')



@app.route('/index.html')
def homepage():
    return render_template('index.html')

@app.route('/aboutus.html') 
def aboutus():  
    return render_template('aboutus.html')

@app.route('/contact.html') 
def contact():  
    return render_template('contact.html')

@app.route('/checkout.html') 
def checkout():  
    return render_template('checkout.html')

@app.route('/orderplace.html') 
def orderplaced():  
    return render_template('orderplace.html')

@app.route('/checkout1.html') 
def checkout1():  
    return render_template('checkout1.html')

@app.route('/checkout2.html') 
def checkout2():  
    return render_template('checkout2.html')

@app.route('/checkout3.html') 
def checkout3():  
    return render_template('checkout3.html')

@app.route('/checkout4.html') 
def checkout4():  
    return render_template('checkout4.html')

@app.route('/shoppingcart.html') 
def shoppingcart():  
    return render_template('shoppingcart.html')

@app.route('/mens/mens.html')
def mens_css():
    return render_template('mens/mens.html')

@app.route('/mens/index.html')
def mens_back():
    return render_template('index.html')

@app.route('/womens.html')
def women():
    return render_template('womens.html')

@app.route('/furniture.html')
def furniture():
    return render_template('furniture.html')

@app.route('/cars.html')
def cars():
    return render_template('cars.html')

@app.route('/others.html')
def others():
    return render_template('others.html')

@app.route('/payments/card.html')
def card():
    return render_template('payments/card.html')

@app.route('/order_placed.html')
def order_placed():
    return render_template('order_placed.html')

@app.route('/payments/order_placed.html')
def order_placed_():
    return render_template('order_placed.html')

@app.route('/payments/pay.html',methods=['GET','POST'])
def pay():
    if request.method=='POST':
         username=request.form.get('username')
         usr_id=request.form.get('usr_id')
         user=User.query.filter_by(usr_id=usr_id).first()
         client=razorpay.Client(auth=('rzp_test_fRz26POs840V1a','2nJWwcX0pnpB5TzfWrxT9XgE'))
         payment=client.order.create({'amount':(int(user.amount*100)),'currency':'INR','payment_capture':'1'})
    return render_template('payments/pay.html',payment=payment)

@app.route('/payments/success.html',methods=['GET','POST'])
def success():
    return render_template('payments/success.html')

  
if __name__ =='__main__':  
    app.run(debug = True, port = 8000,host='0.0.0.0')  

