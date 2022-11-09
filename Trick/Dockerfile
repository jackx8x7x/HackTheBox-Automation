FROM python:latest
RUN python -m pip install --upgrade pip;\
    python -m pip install --upgrade requests;
WORKDIR /app
COPY exploit.py .
ENTRYPOINT ["/app/exploit.py"]
