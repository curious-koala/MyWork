# Nikhar Flask App- Azure Web Service Deployment
Cretaed a flask based app using python that can take input (string) and finds and replaces specific Keywords on the output.

# Replacement Code:

The code essentially works on a list on words. It finds and replaces the word with word+copyright symbol via flask app.

# Infrastructure:
I have used falsk for creating the app in python. I have used Azure web services to host the app. https://nikharflaskapp1.azurewebsites.net
User will get to see the keywords which will be found and replaced in the input queries. 
Github is used for CI/CD implementation of the code into the Azure web App services.

# Query 

Users can put their query and see the results on the endpoint https://nikharflaskapp1.azurewebsites.net/requests?input= (Enter your String).

# Docker Image

The idea is to use Docker images in future developments in order to utilize the concept of containerization of the Web APP. (For now it's just placed here as placeholder and not used in web app deployment CI/CD).


