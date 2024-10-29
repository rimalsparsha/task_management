# Specifies the base image for Python 3.9.
FROM python:3.9

# Ensures output is sent to the terminal without buffering, useful for logging.
ENV PYTHONUNBUFFERED 1  

# Sets the working directory inside the container to /app.
WORKDIR /app  

# Copies the requirements.txt file to the /app directory in the container.
COPY requirements.txt /app/  
# Installs the Python packages specified in requirements.txt.
RUN pip install -r requirements.txt  

# Copies the entire project directory to the /app directory in the container.
COPY . /app/  
