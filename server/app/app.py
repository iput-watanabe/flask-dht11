from flask import Flask, render_template
from get_csv import get_csv_data

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    sensor_data = get_csv_data()
    return render_template('index.html', input_from_python = sensor_data) 

if __name__ == "__main__":  
    app.run(debug=False, host='localhost', port=9999)