from flask import render_template, Flask

app = Flask(__name__, static_folder='C:\\Users\\tanli\\Documents\\GitHub\\LTPythonNC\\Lab07\\Bai09\\templates\\static')

@app.route('/')
def index():
    return render_template("abc.html")

if __name__ == '__main__':
    app.run(port=5450)