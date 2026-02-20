import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "Docker Compose App Running<br>"
        f"DB Host: {os.getenv('DB_HOST')}<br>"
        f"DB Name: {os.getenv('DB_NAME')}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
