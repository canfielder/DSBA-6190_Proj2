![](https://github.com/canfielder/DSBA-6190_Proj2/blob/master/static/kym-ellis-aF1NPSnDQLw-unsplash.jpg)
Photo by Kym Ellis on Unsplash

# DSBA 6190 Project 2
## Dockerized Flask App for Predicting Red Wine Quality Via Sklearn Model
[![CircleCI](https://circleci.com/gh/canfielder/DSBA-6190_Proj2.svg?style=svg)](https://circleci.com/gh/canfielder/DSBA-6190_Proj2)

The followings repo contains a Flask App and a Dockerfile which will containerize the entire app and run the app when called. Additionally, this app is enabled with the necessary files to run a Locust load test. These files were created for UNC Charlotte Spring 2020 DSBA 6190 (Introduction to Cloud Computing) Project 2.

## Flask App
### Model Development
The Flask app runs a sklearn model which predicts red wine quality based on provided input by the user. The input data for this model is the [Wine Quality Data Set](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) from the UCI Machine Learning Repository. The red wine data was used.

The input variables for predicting wine quality are as follows:
1. Fixed Acidity
2. Volatile Acidity
3. Citric Acid
4. Residual Sugar
5. Chlorides
6. Free Sulfur Dioxide
7. Total Sulfur Dioxide
8. Density
9. pH
10. sulphates
11. Alcohol

The output variabale is Quality (0 - 10 scale). 

To determine the sklearn model to be used in the Flask App, four regression models were created and evaluated: linear regression, support vector machines regression, random forest regression, and gradient boost regression. StandardScaler was used to scale the data. Of the four models random forest regression performed the best, with an R<sup>2</sup> of 0.71 and the lowest Root Mean Squared Error of all of the models. As the purpose of this project was to dockerize a Flask App with a python script, the actual quality of the model wasn't essential. Therefore, no further models were or additional data manipulations were pursued. 

The random forest regression model and the StandardScaler object (trained on the training data) were exported via joblib was use in the Flask App. 

The full analysis can be seen in [notebook included in this repo](https://github.com/canfielder/DSBA-6190_Proj2/tree/master/wine_predict).

### Using The App
Once deployed, the app opens on a landing page with a link to page for wine predictions. Entering the requested inputs and selecting Calculate will generate a wine quality score. Note, if no value is input the model will use 0 for that variable.

The following is an example of using the app to generate a win quality score.

![](https://github.com/canfielder/DSBA-6190_Proj2/blob/master/static/2020-02-17%2012_45_29-Predict%20Red%20Wine%20Quality%20with%20Sklearn%20Model.png)

## Docker
A Dockerfile is included in this repo allowing for the containerization of the Flask App with Docker. The container is set up to execute the Flask App when run. The open port to connect to the app is 8080.

The deployed docker container is also found at [Dockerhub](https://hub.docker.com/repository/docker/canfielder/dsba-6190_proj2_docker). 

## Locust Load Test
The required files to run a locust load test were also included in this app. This was an effort to become more familiar with using locust in lead up to the final DSBA 6190 project. 

The folloiwng charts were generated when running 100 users at 1 additional user every half second.

### Number of Users
![Number of Users](https://github.com/canfielder/DSBA-6190_Proj2/blob/master/static/number_of_users_1581880283.png)

### Response Times
![Response Times](https://github.com/canfielder/DSBA-6190_Proj2/blob/master/static/response_times_(ms)_1581880283.png)

### Total Requests per Second
![Total Requests per Second ](https://github.com/canfielder/DSBA-6190_Proj2/blob/master/static/total_requests_per_second_1581880283.png)
