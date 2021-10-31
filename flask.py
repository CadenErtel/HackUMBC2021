from flask import Flask
import requests

flask_app = Flask(__name__)

@flask_app.route("/")
def hello_world():
    r = requests.get(" http://localhost:8501")
    print(r.content)
    return r.content

@flask_app.route("/home")
def home_func():
    return 'home'

def main() -> None:
    flask_app.run(port=5000)

if __name__ == '__main__':
    main()