from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Your Flask App is LIVE on Azure!"

if __name__ == '__main__':
    app.run()
