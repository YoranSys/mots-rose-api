FROM --platform=arm64 python:3
COPY . /app/
WORKDIR /app

RUN pip install -r ./requirements.txt

EXPOSE 8000

ENTRYPOINT [ "uvicorn","--host", "0.0.0.0", "main:app" ]