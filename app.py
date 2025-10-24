from flask import Flask, render_template, request
from decoder import decoder

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=["POST"])
def decode_message():
    text = request.form["message"]
    mode = request.form["mode"]
    result = decoder(text, mode)
    return render_template("index.html", output=result)


if __name__ == "__main__":
    app.run(debug=True)
