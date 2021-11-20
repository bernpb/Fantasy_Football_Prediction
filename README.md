# Fantasy Points Prediction for Offensive Players in the NFL

This project constitutes the final assignment of the Lighthouse Labs data science bootcamp.

The goal of this project is to predict the offensive output of NFL players with respect to the fantasy points they produce.  Fantasy football is an industry valued at over $18 billion with over 60 million players in North America.  As such, there is no shortage of individuals looking to get a competitive edge on the friends, family and co-workers they participate with.

To tackle this challenge, I will be sourcing the bulk of my data from the SportsData.io and MySportsFeeds APIs.  As a regression problem the models I will be trying are simple linear regression, random forest, gradient-boosting trees as well as LSTM neural networks.  As this project is an academic pursuit, I hope to spend some time with each of these techniques to better understand their intricacies.  The model with the best performance will be tuned and finalized. My goal is to predict player output with a mean squared error of 45.

My objective is to deploy my model for demonstration purposes using an AWS EC2 instance with Flask and Dash.  Using this web apploication, a user will be able to input player names either as a string, or list of strings and the app will return their projected fantasy output for their next game.