FROM python:3.10

WORKDIR  src

COPY ./requirements.txt /src/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /src/requirements.txt

COPY * /src/

ENTRYPOINT ["python3"]
CMD ["main.py"]