FROM docker.io/python:3.10.6

WORKDIR /app
 
COPY ./* ./

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]