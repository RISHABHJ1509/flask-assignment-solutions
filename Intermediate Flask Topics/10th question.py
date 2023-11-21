#10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template

app = Flask(__name__)

# Custom error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return "Welcome to the Flask App!"

# Simulate a 500 error by dividing by zero
@app.route('/error')
def simulate_error():
    # This will cause a ZeroDivisionError
    result = 1 / 0
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')
