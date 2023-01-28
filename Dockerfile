FROM continuumio/miniconda3:latest

WORKDIR /twitter_proj

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "twitter_env", "/bin/bash", "-c"]

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "conda", "run", "-n", "twitter_env", "gunicorn", "wsgi:app", "-b", "0.0.0.0:8000"]
