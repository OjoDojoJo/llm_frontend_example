FROM python:3.12-slim

WORKDIR /usr/src/app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["streamlit", "run", "app.py"]