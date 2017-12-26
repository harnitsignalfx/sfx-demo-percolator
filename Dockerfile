FROM python:2

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY requests-handler.py ./

CMD python requests-handler.py
