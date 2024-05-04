
from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/heart_rate_data', methods=['POST'])
def heart_rate_data():
    data = json.loads(request.data)
    heart_rate = data['heart_rate']
    # Update heart rate graph on the watchface
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
