from flask import Flask, render_template
import requests


app = Flask(__name__)#instance

BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts"


@app.route('/')#for homepage
def index():
   
    url = f"{BASE_URL}/random?language=en"
    response = requests.get(url, headers={"Accept": "application/json"})#url for fetching a random fact

         
   
    if response.status_code == 200:
        fact = response.json()["text"]
    else:
        fact = "Sorry, we couldn't fetch a fact at the moment."

    return render_template('index.html', fact=fact)

if __name__ == '__main__':#running the flask
    app.run(debug=True)
