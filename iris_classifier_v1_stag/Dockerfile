# server(backend)
FROM python:3.7

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y vim

COPY . .
EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002" , "--reload"]