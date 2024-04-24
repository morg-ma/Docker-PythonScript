FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY paragraphs.txt .

COPY filtered_text.txt .

COPY script.py .

COPY counter.py .

RUN python script.py

CMD python counter.py