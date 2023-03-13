from flask import Flask, render_template


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

@app.route('/login.php')
def signin_():
    return render_template('login.php')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

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


  
if __name__ =='__main__':  
    app.run(debug = True, port = 8000)  

