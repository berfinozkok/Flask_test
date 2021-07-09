from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return "Welcome!"


@app.route('/berfn')
def berfn():
    return "Hello Berfin!"

if __name__=='__main__':
    app.run(debug=True)