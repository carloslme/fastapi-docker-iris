# model(backend)
FROM python:3.7

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]