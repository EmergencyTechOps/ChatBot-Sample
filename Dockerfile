# Use an official Python runtime as a parent image with Python 3.9
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and model files
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["python", "app.py"]
