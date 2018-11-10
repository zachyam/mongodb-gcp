FROM python:3.6.5

COPY requirements.txt ./

COPY app.py ./

RUN pip install -r requirements.txt

# Run the search loader
ENTRYPOINT [ "python3", "./app.py"]
