import flask
from database import Database
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

app = flask.Flask(__name__)
database = Database()

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/cica')
def cica():
    db = Database.instance.readup_db()
    print(type(db))
    return flask.jsonify(db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))
