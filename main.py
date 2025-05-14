from flask import Flask, render_template

# create website instance
app = Flask(__name__)


# web pages
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def translate(word):
    return {"defination": word.upper(),
            "word": word}


# run application
if __name__ == "__main__":
    app.run(debug=True)
