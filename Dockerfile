FROM python:3.12.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py" , "run", "--port", "5500"]
