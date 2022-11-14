FROM python:latest
RUN python -m pip install --upgrade pip;\
    python -m pip install requests pyjwt
WORKDIR /app
COPY exploit.py .
ENTRYPOINT ["/app/exploit.py"]
