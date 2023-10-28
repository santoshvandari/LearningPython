from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Index HTML</h1>
            <h1>Created Using Flask</h1>
        </body>
        </html>

'''