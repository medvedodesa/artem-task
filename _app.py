from flask import Flask


app = Flask(__name__)
UPLOAD_FOLDER = '/'

if __name__ == '__main__':
    app.run()





app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER