
from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return "<h1>Hello flask </h1>"
if __name__== "__main__":
    app.run(debug=True)
