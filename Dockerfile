FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the port (matches docker-compose.yml)
EXPOSE 8000

# Set the entrypoint to run mail.py
CMD ["python", "main.py"]