from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("gender_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]

    name = name.lower()

    data = vectorizer.transform([name])

    prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        name=name.title(),
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)