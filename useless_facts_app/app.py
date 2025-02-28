from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Function to get a useless fact
def get_useless_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["text"]
    return "Could not fetch fact."

# Function to get a random meme
def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    if response.status_code == 200:
        meme_data = response.json()
        return {"title": meme_data["title"], "url": meme_data["url"], "postLink": meme_data["postLink"]}
    return {"title": "Could not fetch meme.", "url": "", "postLink": ""}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/facts")
def facts():
    fact = get_useless_fact()
    return render_template("facts.html", fact=fact)

@app.route("/memes")
def memes():
    meme = get_meme()
    return render_template("memes.html", meme=meme)

@app.route("/get-fact")
def fetch_fact():
    return jsonify({"fact": get_useless_fact()})

@app.route("/get-meme")
def fetch_meme():
    return jsonify(get_meme())

if __name__ == "__main__":
    app.run(debug=True)
