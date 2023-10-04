from flask import Flask

app = Flask("My first application")


@app.route('/')

def hello():
    return("hi im bhavinnn")


if __name__=="__main__":
    app.run(debug=True)
