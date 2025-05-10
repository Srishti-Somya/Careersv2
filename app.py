from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # decorator added when url / is accessed then show hello_world()
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
