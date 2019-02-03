FROM python:latest
COPY . /tmp/slackbot
RUN pip install slackbot
CMD ["python", "/tmp/slackbot/run.py"]
