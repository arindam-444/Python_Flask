from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/test1")

@app.route("/")
def test():
    return "<h1>Wlcome in Python Flask</h1>"
def test1():
    return "<h1>I am a good boy</h1>"

@app.route("/test2")
def test2():
    return "<h1> good boy</h1>"

@app.route("/test3")
def test3():
    data=request.args.get('x')
    return "MY name is{}".format(data)

if __name__=="__main__" :
    app.run(host="0.0.0.0")