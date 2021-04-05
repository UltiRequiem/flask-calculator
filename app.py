from flask import Flask, render_template, request
from keep_alive import keep_alive, app

@app.route('/')
def main():
    return render_template("main.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    number_one = request.form['number_one']
    number_two = request.form['number_two']
    operation = request.form['operation']

    if operation == 'add':
        try:
            result = float(number_one) + float(number_two)
            return render_template('main.html', result=result)
        except ValueError:
            result = "Please enter an integer"
            return render_template('main.html', result=result)

    elif operation == 'subtract':
        result = float(number_one) - float(number_two)
        return render_template('main.html', result=result)

    elif operation == 'multiply':
        try:
            result = float(number_one) * float(number_two)
            return render_template('main.html', result=result)
        except ValueError:
            result = "Please enter an integer"
            return render_template('main.html', result=result)

    elif operation == 'divide':
        try:
            result = float(number_one) / float(number_two)
            return render_template('main.html', result=result)
        except ValueError:
            result = "Please enter an integer"
            return render_template('main.html', result=result)
    else:
        return render_template('main.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

if __name__ == '__main__':
    keep_alive()
