# Use an official Python image, specifying a version that supports both ARM and AMD architectures.
FROM python:3.10.11 AS build

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install required packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["gunicorn","--bind","0.0.0.0:8080","app:app"]