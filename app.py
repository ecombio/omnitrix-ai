from flask import Flask, request, jsonify, render_template
from search_engine import google_search

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    results = google_search(query)
    return jsonify({"query": query, "results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
