from flask import Flask,render_template
app=Flask(__name__)
db=[
    {'author':'John Greesham','date_of_published':'09-10-2002',
     'title':'How to success without any struggle'
     },
    {
    'author':'Balayya','date_of_published':'09-10-1995',
    'title':'Dont trouble the trouble'
    }
]
@app.route('/')

def home():
    return render_template('home.html',posts=db)
@app.route('/about')
def about():
    return render_template('about.html',title='About US')
if __name__== "__main__":
    app.run(debug=True)