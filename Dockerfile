FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN python3 -m pip install Pillow

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]