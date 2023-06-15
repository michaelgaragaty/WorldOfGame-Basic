FROM python:alpine3.17
RUN pip install flask
COPY MainScores.py Score.py Utils.py ./app/
COPY ./templates/* ./app/templates/
WORKDIR /app
VOLUME /app/Scores.txt
EXPOSE 5000
ENTRYPOINT ["python", "/app/MainScores.py"]