from flask import Flask, render_template
import csv

app = Flask(__name__)

with open('dictionary.csv', 'r', encoding='utf-8') as f:
    my_dictionary = csv.reader(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def dicti(word):
    new = [row[1] for row in my_dictionary if row[0] == word]
    for i in new:
        if i == 'definition':
            new.remove('definition')
    definition_with_linebreaks = new[0].replace('\n', '<br>')
    wrap = {"word": str(word).title(),
            "definition": definition_with_linebreaks}
    return wrap


if __name__ == "__main__":
    app.run(debug=True, port=5001)
