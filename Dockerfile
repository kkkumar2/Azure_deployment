FROM python:3.10-slim-buster
# RUN mkdir /opt/stream
# WORKDIR  /opt/stream

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .
EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]