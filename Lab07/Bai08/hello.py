from flask import render_template, Flask

app = Flask(__name__)

languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
languages.append({'STT':4, 'ten': ".NET" })
languages.append({'STT':5, 'ten': "Matlab" })

@app.route('/languages')
def index():
    return render_template("abc.html", ngon_ngu = languages)

if __name__ == '__main__':
    app.run(port=5002)