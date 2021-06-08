from flask import render_template, request
from keep_alive import keep_alive, app


@app.route("/")
def main():
    return render_template("calculator.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number_one = request.form["number_one"]
    number_two = request.form["number_two"]
    operation = request.form["operation"]

    if operation == "add":
        result = float(number_one) + float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "subtract":
        result = float(number_one) - float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "multiply":
        result = float(number_one) * float(number_two)
        return render_template("calculator.html", result=result)

    elif operation == "divide":
        result = float(number_one) / float(number_two)
        return render_template("calculator.html", result=result)

    else:
        return render_template("calculator.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)


if __name__ == "__main__":
    keep_alive()
