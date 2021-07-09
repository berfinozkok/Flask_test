from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return "Welcome!"


@app.route('/berfn')
def berfn():
    return "Hello Berfin!"

@app.route('/Ask_mail')
def Ask_mail():
    return "Enter your e-mail:"


if __name__=='__main__':
    app.run(debug=True)