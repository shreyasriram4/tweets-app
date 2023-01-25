# Recent Tweets Viewer

A very basic web application I built to learn a few new skills!

I used Flask to build the front-end, and the Twitter API back-end to access tweets.

### Instructions:

1. Install dependencies as follows (ideally in a virtual environment)

```bash
pip install -r requirements.txt
```

Or, if the file is not available, try:

```bash
pip install Flask==2.2.2
pip install gunicorn==20.1.0
pip install pandas==1.5.3
pip install tweepy==4.12.1
```

2. Run Flask app

```bash
flask run
```

3. Run localhost server: http://127.0.0.1:5000

Currently working on deploying on Docker, hence the Dockerfile.
