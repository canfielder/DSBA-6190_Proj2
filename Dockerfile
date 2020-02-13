FROM python:3.7.3-stretch

# Working Directory
WORKDIR /main

# Copy source code to working directory
COPY . main.py /main/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

# Run main.py at container launch
CMD ["python", "main.py"]