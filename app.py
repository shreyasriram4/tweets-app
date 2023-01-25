from flask import Flask, render_template, request
from utils import username_tweets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods= ['POST'])
def final():
    username = request.form['username']
    count = request.form['count']
    df = username_tweets(username, count)
    return render_template('result.html', data = df.to_html())

if __name__ == "__main__":
   app.run(debug=True)