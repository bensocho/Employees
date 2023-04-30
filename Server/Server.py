from flask import Flask
import requests

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def health_check():
    return "healthy"

if __name__ == "__main__":
    app.run(debug=True)
