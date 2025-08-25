from app import app


@app.route("/hello")
def hello():
    return "Hello, world!"


@app.route("/info")
def info():
    return "This is an informational page."


@app.route("/calc/<int:number1>/<int:number2>")
def calc(number1, number2):
    return f"The sum of {number1} and {number2} is {number1+number2}."


@app.route("/reverse/<text>")
def user_profile(text):
    return f"{text[::-1]}"


@app.route("/user/<name>/<int:age>")
def user(name, age):
    return f"Hello, {name}. You are {age} years old."