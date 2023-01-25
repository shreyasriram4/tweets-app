FROM python:3.8-slim-buster

WORKDIR /twitter_proj

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "-m" , "flask", "run", "--host=0.0.0.0"]
