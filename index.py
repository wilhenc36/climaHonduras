from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():   
    if request.method == 'POST':
        ciudad = request.form['city']
        APIkey = 'fffd1d621a3df95655eb9feb1938dbb4'
        pais = 'hn'
        URI = (f'https://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={APIkey}&units=metric&lang=es')
        response = requests.get(URI)
        response_json = response.json()
        if(response_json["cod"] == 200):
            weather = [{'city':response_json['name'], 'country':response_json['sys']['country'], 'description':response_json['weather'][0]['description'], 'temp':response_json['main']['temp'], 'humidity':response_json['main']['humidity'], 'speed_wind':response_json['wind']['speed']}]
        else:
            weather = ""
        return render_template("index.html", weather=weather)
    
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run() 