FROM python:3.12-slim
 
WORKDIR /app
 
# libgomp1 is needed by some xgboost/catboost builds for OpenMP support
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*
 
COPY requirment.txt .
RUN pip install --no-cache-dir -r requirment.txt
 
COPY . .
 
EXPOSE 5000
 
# Use gunicorn in production instead of the Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:application"]