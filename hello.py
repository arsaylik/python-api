from flask import Flask, render_template, request, jsonify
from deneme import get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return jsonify(weather_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
