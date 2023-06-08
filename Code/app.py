"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from histogram_class import Histogram


app = Flask(__name__)
histogram = Histogram("./Code/story.txt")

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = histogram._generate_random_sentence()
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
