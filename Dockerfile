FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "-c", "alembic upgrade head && python main.py"]
