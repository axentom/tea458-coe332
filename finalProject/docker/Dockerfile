# Image: axentom/axentom_web:finalProject
FROM python:3.9

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY api.py /app/
COPY jobs.py /app/
COPY worker.py /app/
WORKDIR /app/

CMD python /app/api.py
