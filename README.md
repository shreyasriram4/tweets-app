# Recent Tweets Viewer

A very basic web application I built to learn a few new skills!

I used Flask to build the front-end, and the Twitter API back-end to access tweets. Gunicorn is used for its ability to concurrently run multiple threads of the app.

## Instructions:

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

2. Run Flask app using Gunicorn server

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app 
```

3. Run localhost server: http://0.0.0.0:5000/

## Docker Implementation Instructions

Alternatively, I have containerised the entire repository using Docker, so if you have Docker installed, these instructions may be easier to follow:

1. Once in the repository, simply enter this command in the terminal while running your Docker daemon:

```bash
docker-compose up -d
```

2. Identify ports in use. 

```bash
docker ps
```

3. Then run localhost server based on ports specified

Currently, I am still figuring out how to fix the internal port without running into errors. TBC!
