# Base image Python 3.9 use kar rahe hain
FROM python:3.9-slim

# Container ke andar working directory set karna
WORKDIR /app

# Requirements file copy karna aur libraries install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pura project code (model, data, api) container mein copy karna
COPY . .

# FastAPI ka port expose karna
EXPOSE 8000

# Container start hone par API server chalane ki command
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]