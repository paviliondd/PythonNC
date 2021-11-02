from flask import render_template, Flask

app = Flask(__name__)

@app.route('/hello')

@app.route('/hello/<name>')
def index(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(port=5000)