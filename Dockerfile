FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python", "./discord.py"]