from flask import Flask, redirect, abort, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

if __name__ == '__main__':
    app.run(port=5000)