from flask import Flask

app = Flask(__name__)

@app.route('/hello/<string:name>')
def say_hello(name):
    get_name = name
    return f"hello {get_name}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
