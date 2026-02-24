from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Sourabh 👋 Python deployment successful on Azure!"

if __name__ == "__main__":
    app.run()