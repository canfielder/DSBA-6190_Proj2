FROM python:3.7.3-alpine

# Working Directory
WORKDIR /app

# Copy source code to working directory
#COPY . app.py /app/
COPY requirements.txt .

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 80
EXPOSE 80

# Run main.py at container launch
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]