from flask import Flask, render_template, jsonify
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
def home():
    return render_template('index.html')

@app.route('/fact')  # Fact page route
def fact_page():
    fact = get_useless_fact()
    return render_template('fact.html', fact=fact)

@app.route('/meme')  # Meme page route
def meme_page():
    meme = get_meme()
    return render_template('meme.html', meme=meme)

@app.route('/api/fact')  # API endpoint for AJAX fact fetching
def get_fact_api():
    return jsonify({"fact": get_useless_fact()})

@app.route('/api/meme')  # API endpoint for AJAX meme fetching
def get_meme_api():
    return jsonify(get_meme())

if __name__ == '__main__':  # Run the Flask app
    app.run(debug=True)
