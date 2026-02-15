from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>welcome to my website</h1>"

@app.route("/study")
def study():
    return "<h1>i am currently studying cloud computing technology</h1>"


@app.route("/mum")
def mum():
    return "<h3>i love my mum so much and she is the best thing that could happen to me</h3>"

@app.route("/town")
def town():
    return "<h3>i am currently in port harcourt</h3>"

@app.route("/add")
def add():
    a=89
    b=69
    c=a+b
    return "<h1>this is the addition</h1> "+ str(c)

@app.route("/subtract")
def subtract():
    a=89
    b=69
    c=a-b
    return "<h3>this is the subtraction</h3> "+ str(c)

@app.route("/multiply")
def multiply():
    a=89
    b=69
    c=a*b
    return "<h3>this is the multiplication</h3> "+ str(c)

@app.route("/divide")
def division():
    a=89
    b=69
    c=a/b
    return "<h3>this is the division</h3> "+ str(c)

@app.route("/calculation")
def calculation():
    a=31
    b=51
    c=31
    d=a*b*c
    e=1500/d
    f=2000+e
    if f>20000:
        g=f-5000
    else:
        g=f+10000
            
    return "<h3>this is the calculation</h3> "+ str(g)

@app.route('/homepage')
def homepage():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    collect="Details are:" +str(email) +str(name)
    return render_template('homepage.html', collect=collect)
    























if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)