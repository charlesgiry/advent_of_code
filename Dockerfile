FROM python:3-alpine

WORKDIR "/code/"
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
ENTRYPOINT python3 aoc.py
