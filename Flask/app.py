from flask import Flask, jsonify, request
from diseasePredictor import get_disease
import numpy as np
from flask_cors import CORS , cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})




@app.route('/data', methods=['GET'])
def get_query_string():
    symptoms = []
    for i in range(1,6):
        symptom = "s"+str(i)
        symptoms.append(request.args.get(symptom))

    disease_dt = get_disease(symptoms)


    try:
        return jsonify({'status':200,'disease':disease_dt}) 
    except:
        return jsonify({'status':401,'disease': 'Not Found'}) 


        



if __name__ == '__main__':
    app.run(debug=True)