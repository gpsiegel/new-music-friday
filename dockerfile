FROM python:3.8-alpine3.13

WORKDIR C:\\<path>

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
