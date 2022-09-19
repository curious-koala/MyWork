# For more information, please refer to https://aka.ms/vscode-docker-python
#use python for base image
FROM python:3.8.0-slim

# USe working directory /app
WORKDIR /app


# Install pip requirements
COPY './requirements.txt' .

#run pip installation 
RUN python -m pip install -r requirements.txt

#copy everything
COPY . .

#define entrypoints
ENTRYPOINT ["python", "app.py"]
