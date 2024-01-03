# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Flask, Gunicorn, and other required packages
RUN pip install Flask gunicorn pandas scikit-learn

# Expose the port the app runs on
EXPOSE 9696

# Run the app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9696", "Predict:app"]
