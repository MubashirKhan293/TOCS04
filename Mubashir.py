from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    return ('Assignment 04 of TOCS..')

if __name__ == '__main__':
    app.run()
