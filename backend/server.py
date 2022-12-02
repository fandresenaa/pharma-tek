from flask import Flask

app = Flask(__name__)

#Route voloany
@app.route('/')
def home():
    return('gg , ao amle API tsika ')

if __name__ == '__main__':
    app.run(debug=True)