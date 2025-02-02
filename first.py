
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/hello')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__== "__main__":
    app.run(debug=True)
why we should use render_templates
Final Thought:
render_template() is essential for building Flask web applications efficiently.
It helps in dynamic content rendering, code reusability, and keeping Python code clean.
    
