from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("redirect.html")
    return render_template("index.html")

@app.route("/redirect.html")
def redirect_page():
    return render_template("redirect.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


