from flask import Flask

app = Flask(__name__)

@app.route("/api/get-data", methods=["GET"])
def main():
    return ({"data" : "Hi There!"})