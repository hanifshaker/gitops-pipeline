from flask import Flask, render_template, request, jsonify


app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    return jsonify({
        "message": f"Hello, {name}!"
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )