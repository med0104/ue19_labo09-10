FROM python
RUN pip install requests
WORKDIR /app
COPY . /app
CMD ["python3", "app.py"]