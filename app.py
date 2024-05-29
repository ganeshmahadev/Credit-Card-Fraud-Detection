from flask import Flask, request, jsonify, render_template
import pickle as pkl
import numpy as np

# Load the pipeline
with open("pipeline.pkl", 'rb') as file:
    pipeline = pkl.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    data_values = np.array(data["data"]).reshape(1, -1)
    
    prediction = pipeline.predict(data_values)
    
    return jsonify({
        "prediction": prediction[0]
    })

if __name__ == '__main__':
    app.run(debug=True)
