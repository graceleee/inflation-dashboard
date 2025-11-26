FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose the port Flask runs on
EXPOSE 5050
CMD ["python", "src/app.py"]