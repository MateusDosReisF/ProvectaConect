FROM python:3.11-slim

WORKDIR /ProvectaConect

COPY requirements.txt /ProvectaConect/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /ProvectaConect/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]