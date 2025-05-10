from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
  {
    'id' : 1,
    'title': 'RustDB',
    'completed': 'Ongoing',
  },
  {
    'id' : 2,
    'title': 'AI Data Curator',
    'completed': 'Nov 2024',
  },
  {
    'id' : 3,
    'title': 'Language Translator',
    'completed': 'Dec 2023',
  },
]


@app.route("/")  # decorator added when url / is accessed then show hello_world()
def hello_world():
  return render_template("home.html", projects = PROJECTS)

@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
