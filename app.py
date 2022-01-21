from flask import Flask, render_template
import scrapping

app = Flask(__name__)

@app.route('/')
def hola():
    return render_template('index.html',news=scrapping.last_five_tecno_news())