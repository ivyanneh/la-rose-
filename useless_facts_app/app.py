from flask import Flask, render_template
import requests

app = Flask(__name__)  # Instance of Flask

# API Endpoints
FACTS_API_URL = "https://uselessfacts.jsph.pl/api/v2/facts"
MEME_API_URL = "https://meme-api.com/gimme"

# Function to get a useless fact
def get_useless_fact():
    url = f"{FACTS_API_URL}/random?language=en"
    response = requests.get(url, headers={"Accept": "application/json"})

    if response.status_code == 200:
        return response.json()["text"]
    return "Sorry, we couldn't fetch a fact at the moment."

# Function to get a random meme
def get_meme():
    response = requests.get(MEME_API_URL)
    
    if response.status_code == 200:
        meme_data = response.json()
        return {
            "title": meme_data.get("title", "Funny Meme"),
            "url": meme_data.get("url", ""),
            "postLink": meme_data.get("postLink", "#")
        }
    return {
        "title": "Sorry, couldn't fetch a meme.",
        "url": "",
        "postLink": "#"
    }

@app.route('/')  # Homepage route
def index():
    fact = get_useless_fact()  # Fetch a useless fact
    meme = get_meme()  # Fetch a random meme
    return render_template('index.html', fact=fact, meme=meme)  # Send data to HTML

if __name__ == '__main__':  # Run the Flask app
    app.run(debug=True)
