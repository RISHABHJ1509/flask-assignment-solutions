from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello, {username}!'

if __name__=='__main__':
    app.run(host='0.0.0.0')
