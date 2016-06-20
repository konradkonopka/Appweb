import os
from pandas import json
from pprint import pprint
import pandas as pd
from subprocess import call

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    plec = db.Column(db.Text, nullable=False)
    wiek = db.Column(db.Text)
    zarobki = db.Column(db.Text)
    oczekiwania = db.Column(db.Text)
    staz = db.Column(db.Text)
    ostpodw = db.Column(db.Text)
    zadowolenie = db.Column(db.Text)
    zmianapracy = db.Column(db.Text)
    htyg = db.Column(db.Text)

    def __init__(self, plec, wiek, zarobki, oczekiwania, staz, ostpodw , zadowolenie, zmianapracy, htyg):
        self.plec = plec
        self.wiek = wiek
        self.zarobki = zarobki
        self.oczekiwania = oczekiwania
        self.staz = staz
        self.ostpodw = ostpodw
        self.zadowolenie = zadowolenie
        self.zmianapracy = zmianapracy
        self.htyg = htyg
db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/data")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('data.html', formdata=fd)

@app.route("/result")
def show_result():
    print ("before")
    os.system("python ../dirbot/spiders/webcrawler.py 1")
    print ("after")

    with open('result.json') as data_file:
        data = json.load(data_file)

        plec = []
        wiek = []
        wiekrozpoczecia = []
        wiekdiagnozy = []
        czastrwania = []
        edss = []
        kursms = []
        nawrot12 = []
        nawrot24 = []

        for x in data:
            v1 = x["typ"]
            v2 = x["opis"]
            v3 = x["ilosc"]
            v1 = " ".join(str(v) for v in v1)
            v2 = " ".join(str(v) for v in v2)
            v3 = " ".join(str(v) for v in v3)
            if v1 == "Distribution of gender":
                plec.extend([[v2, int(v3)]])
            if v1 == "Age":
                wiek.extend([[v2,int(v3)]])
            if v1 == "Age at onset":
                wiekrozpoczecia.extend([[v2,int(v3)]])
            if v1 == "Age at diagnosis":
                wiekdiagnozy.extend([[v2, int(v3)]])
            if v1 == "Duration of MS":
                czastrwania.extend([[v2, int(v3)]])
            if v1 == "EDSS at last visit":
                edss.extend([[v2, int(v3)]])
            if v1 == "Last MSCourse":
                kursms.extend([[v2, int(v3)]])
            if v1 == "Relapse count over last 12 months":
                nawrot12.extend([[v2, int(v3)]])
            if v1 == "Relapse count over last 24 months":
                nawrot24.extend([[v2, int(v3)]])

        my_dict={'plec': plec, 'wiek': wiek, 'wiekrozpoczecia':wiekrozpoczecia, 'wiekdiagnozy': wiekdiagnozy,'czastrwania': czastrwania, 'edss': edss,'kursms': kursms,'nawrot12': nawrot12,'nawrot24': nawrot24}
        return render_template('result.html', my_dict=my_dict)

# [id_name, dane[id_name][1], 1],
# [id_name, dane[id_name][2], 1],
# [wiek_name, dane[wiek_name][1], 1],]
@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    plec = request.form['plec']
    wiek = request.form['wiek']
    zarobki = request.form['zarobki']
    oczekiwania = request.form['oczekiwania']
    staz = request.form['staz']
    ostpodw = request.form['ostpodw']
    zadowolenie = request.form['zadowolenie']
    zmianapracy = request.form['zmianapracy']
    htyg = request.form['htyg']


    # Save the data
    fd = Formdata(plec, wiek, zarobki, oczekiwania, staz, ostpodw , zadowolenie, zmianapracy, htyg)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    # app.debug = True
    # app.run()

    app.debug = False
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)