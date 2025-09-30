FROM python:3.12-slim

RUN mkdir -p /Filonenko
WORKDIR /Filonenko

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/req.txt
RUN pip install --no-cache-dir -r /tmp/req.txt

COPY app.py /Filonenko/app.py

CMD ["python", "/Filonenko/app.py"]
