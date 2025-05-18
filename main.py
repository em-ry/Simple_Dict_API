from flask import Flask, render_template
import pandas as pd

# create website instance
app = Flask(__name__)


# web pages
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def translate(word):
    df = pd.read_csv("dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"Definition": definition,
            "word": word.title()}


# run application
if __name__ == "__main__":
    app.run(debug=True)
