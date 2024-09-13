from flask import Flask,render_template

api = Flask(__name__)
utenti = [['mario','rossi','M'],['gianni','derossi','M'],['Anita','Garibaldi','F']]


@api.route('/', methods = ['GET'])
def index():
    return render_template("index.html")


@api.route('/regok', methods = ['GET'])
def regok():
    return render_template("reg_ok.html")


@api.route('/regko', methods = ['GET'])
def regko():
    return render_template("reg_ko.html")

@api.route('/registrati', methods = ['GET'])
def registrati():
    return render_template("reg_ko.html")

api.run(host="0.0.0.0",port=8085)