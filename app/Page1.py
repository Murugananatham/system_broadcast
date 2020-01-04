from flask import Flask, render_template
app=Flask(__name__)

posts=[
    {
        'author':'Ramany',
        'college':'psgtech'
    },

    {
        'author':'tharani',
        'college':'psgr'
    },

    {'author':'abc',
     'college':'ABC'
     }
]



@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html",title="Login")

@app.route('/home')
def home():
   return render_template("home.html",posts=posts)

@app.route('/email_broadcasting')
def email_broadcasting():
   return render_template("email_broadcasting.html") 


if __name__=="__main__":
    app.run(debug=True)

