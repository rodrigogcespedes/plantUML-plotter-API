FROM python:3.10

ENV SRC_DIR /usr/bin/src/webapp/src

COPY app2yaml.py ${SRC_DIR}/

COPY requirements.txt ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED=1

EXPOSE 9550

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "uvicorn", "app2yaml:app", "--host", "0.0.0.0", "--port", "9550", "--reload"]