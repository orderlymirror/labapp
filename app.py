from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "app is now live on azuree"

if __name__ == '__main__':
    app.run()
