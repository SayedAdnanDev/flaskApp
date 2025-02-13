from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Thank you Mr Abdullah For The Informative Course :-)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
