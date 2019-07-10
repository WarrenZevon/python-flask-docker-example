import pickle
import os
from os import listdir
from os.path import isfile, join
from flask import Flask, jsonify, request
import numpy as np


app = Flask(__name__)


def load_models():
    models_list = {}
    print('Start loading models from ./models folder...')
    for model_file in [f for f in listdir('./models') if isfile(join('./models', f))]:
        with open('models/' + model_file, 'rb') as f:
            print('Loading ', model_file)
            models_list[os.path.splitext(model_file)[0]] = (pickle.load(f))

    print(models_list.__len__(),'model(s) loaded.')
    return models_list


models = load_models()
labels = ['red','blue']


# GET - /models/list
@app.route('/models/list', methods=['GET'])
def get_models_list():
    return jsonify([*models.keys()])

# POST - /predict/<model_name> with post body
@app.route('/predict/<model_name>', methods=['POST'])
def get_rate_recommendations(model_name: str):

    response = {}

    try:
        model = models[model_name]
    except:
        return jsonify('No model found')

    try:
        post_data = request.get_json()
        x1 = post_data['x1']
        x2 = post_data['x2']

        point_to_predict = np.array([float(x1),float(x2)]).reshape(1, -1)
    
        prediction = model.predict(point_to_predict)[0]
        response['prediction'] = int(prediction)
        response['prediction_label'] = labels[int(prediction)]

        return jsonify(response)

    except: return jsonify('Something went wrong with the prediction')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)        # Use 0.0.0.0 for Docker