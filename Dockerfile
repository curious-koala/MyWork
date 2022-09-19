# For more information, please refer to https://aka.ms/vscode-docker-python
#use python for base image
FROM python:3.8-slim

# USe working directory /app
WORKDIR  /app
#Copy all the current directory content to app
COPY  './requirements.txt' .

# Install pip requirements
#COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
