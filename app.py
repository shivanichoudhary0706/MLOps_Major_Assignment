from flask import Flask, render_template, request
import joblib
import numpy as np
from PIL import Image

app = Flask(__name__)

model, X_test, y_test = joblib.load("savedmodel.pth")

@app.route("/")
def index():
    return "Upload endpoint not implemented in detail, but model loads successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
