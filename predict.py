from flask import Flask
import joblib
from flask import request, jsonify
import numpy as np
import pandas as pd

app = Flask('predict')


with open('model=13.bin', 'rb') as f_in:
    en, dv, model = joblib.load(f_in)

ordered = ['cut', 'color', 'clarity']


app = Flask('diamonds')


@app.route('/predict', methods=['POST'])
def predict():
    diamond = request.get_json()
    diamond = pd.DataFrame([diamond])
    diamond[ordered] = en.transform(diamond[ordered])
    X_dict = diamond.to_dict(orient='records')
    X = dv.transform(X_dict)
    y_pred = model.predict(X)
    price = np.exp(y_pred)

    result = {
        'Value': round(float(price), 3)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

