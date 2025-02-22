from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('profile.html', name="Vladimir Pakhomov", bio="Backend developer that making this homework.")

if __name__ == '__main__':
    app.run()
