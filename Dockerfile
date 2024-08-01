FROM python:3.11-slim
WORKDIR /app
COPY cat_facts.py .
RUN pip install requests
CMD ["python", "cat_facts.py"]
