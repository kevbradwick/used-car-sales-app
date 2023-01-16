import pathlib as pl

import pandas as pd
import skops.io as sio
from flask import Flask, jsonify, request

app = Flask(__name__)

with open(str(pl.Path(__file__).parent.resolve() / "model/model.bin"), "rb") as fp:
    model = sio.loads(fp.read(), trusted=True)


@app.get("/")
def index():
    year = request.args.get("year", "")
    mileage = request.args.get("mileage", "")

    if not all([year, mileage]):
        return jsonify({"error": "missing args"}), 400

    data = {
        "year": [int(year)],
        "mileage": [int(mileage)],
    }

    df = pd.DataFrame(data=data)
    predictions = model.predict(df)
    return jsonify({"prediction": predictions[0]})
