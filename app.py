from flask import Flask

app = Flask(__name__)

@app.route('/hello/<string:name>')
def say_hello(name):
    get_name = name
    return f"hello {get_name}"
