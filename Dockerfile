FROM  python:3.9

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir /samubackend

WORKDIR /samubackend

COPY requirements.txt /samubackend/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /samubackend/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]


