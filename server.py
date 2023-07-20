from flask import Flask, render_template, request
from machinetranslations import translator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/EnglishToFrench')
def engtofre():
    return render_template("EnglishToFrench.html")


@app.route('/FrenchToEnglish')
def fretoeng():
    return render_template("FrenchToEnglish.html")

@app.route('/answer', methods=['POST'])
def answ():
    if request.form.get('val2') == None:
        name = request.form.get('val1')
        value = translator.englishtofrench(name)
    else:
        name = request.form.get('val2')
        value = translator.frenchtoenglish(name) 
    return value

    
app.run(debug = True, port=5000)
