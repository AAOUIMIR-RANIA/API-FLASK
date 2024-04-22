from flask import Flask, render_template
import getData

app=Flask(__name__)


@app.route("/")
def home():
     return render_template('home.html', dateLyouma=getData.dateLyouma2,lyouma=getData.Lyouma,datameteo=getData.dataMeteo2)