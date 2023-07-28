from flask import Flask, redirect, url_for, request, render_template, session 
app = Flask(__name__)

@app.route('/', methods= ['GET'])
def index ():
    return render_template('index.html')

@app.route('/about', methods= ['GET'])
def about():
    return render_template('about.html')

@app.route('/product', methods= ['GET'])
def product():
    return render_template('product.html')

@app.route('/contact', methods= ['GET'])
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
 app.run(debug=True)







