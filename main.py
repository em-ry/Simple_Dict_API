from flask import Flask, render_template
import pandas as pd

# create website instance
app = Flask(__name__)

# Read dict data
df = pd.read_csv("dictionary.csv")


# web pages
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def translate(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"Definition": definition,
            "word": word.title()}


# run application
if __name__ == "__main__":
    app.run(debug=True)
