FROM python:3.9.4
MAINTAINER Jesus
# ADD main.py
COPY app /app
WORKDIR \app

# COPY requirements.txt . ./
RUN pip install -r requirements.txt
# RUn pip install requests

COPY . .

CMD ["python", "main.py"]