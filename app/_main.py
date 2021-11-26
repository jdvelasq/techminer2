from flask import Flask, request, flash, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"


@app.route("/", methods=("GET", "POST"))
@app.route("/index", methods=("GET", "POST"))
def index():

    selected = None

    if request.method == "POST":
        selected = request.form["region"]
        flash(selected)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#
