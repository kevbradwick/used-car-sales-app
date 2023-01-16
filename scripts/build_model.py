import pathlib as pl

import pandas as pd
import skops.io as sio
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

MODEL_DIR = pl.Path(__file__).parent.parent.resolve() / "model"

MODEL_OUT = MODEL_DIR / "model.bin"

df = pd.read_json(MODEL_DIR / "2023-01-10_Audi_A3.json")
df.dropna(inplace=True)

X = df[["year", "mileage"]]
y = df["price"]

# splits the data set in two, one for training and the other for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

accuracy = r2_score(y_test, model.predict(X_test)) * 100
print("💯 Model accuracy: %.2f percent" % accuracy)

obj = sio.dumps(model)

with open(str(MODEL_OUT), "wb") as fp:
    fp.write(obj)
    print(f"🤖 Saved model to {MODEL_OUT}")
