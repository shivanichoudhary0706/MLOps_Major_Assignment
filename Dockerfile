FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# increase timeout to avoid download failure
RUN pip install --default-timeout=200 -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
