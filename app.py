from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "insert_your_api_key"
}

@app.route("/")
def get_started():
    return render_template('index.html')

@app.route("/random")
def random():
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random":"true"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return(response.text)

@app.route('/words/<string:word_in>/frequency')
def frequency(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/frequency".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)

@app.route('/words/<string:word_in>/syllables')
def syllables(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/syllables".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)

@app.route('/words/<string:word_in>/pronunciation')
def pronunciation(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/pronunciation".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)

@app.route('/words/<string:word_in>/rhymes')
def rhymes(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/rhymes".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)

@app.route('/words/<string:word_in>/examples')
def examples(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/examples".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)

@app.route('/words/<string:word_in>/definitions')
def definitions(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)

@app.route('/words/<string:word_in>/synonyms')
def synonyms(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/synonyms".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)    

@app.route('/words/<string:word_in>/antonyms')
def antonyms(word_in: str):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/antonyms".format(word_in)
    response = requests.request("GET", url, headers=headers)
    return(response.text)    


if __name__ == "__main__":
    app.run(host='0.0.0.0')
