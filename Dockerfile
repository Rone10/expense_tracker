# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# RUN mkdir -p /home/app

# Create the app user
# RUN addgroup --system app && adduser --system --group app

# Create the appropriate directories
# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/staticfiles
# # RUN mkdir $APP_HOME/mediafiles
# WORKDIR $APP_HOME

# Set the working directory to /app
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /code


# Make port 8000 available to the world outside this container
EXPOSE 8000

# change to the app user
# USER code

# Run gunicorn when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn",  "expense_tracker.wsgi:application"]