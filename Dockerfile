FROM python:3 AS builder
FROM python:3.9
COPY requirements.txt .
ADD Main.py /
ADD OCR.py /
ADD Linguist.py /
ENV PATH=/root/.local:$PATH
RUN pip install pystrich
RUN pip install requests
RUN pip install psycopg2
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
CMD [ "python", "Main.py" ]