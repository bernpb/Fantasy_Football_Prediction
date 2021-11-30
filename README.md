# Fantasy Point Prediction for Offensive Players in the NFL

## Introduction
This project constitutes the final assignment of the Lighthouse Labs data science bootcamp.

The goal of this project is was to predict the offensive output of NFL players with respect to the fantasy points they produce in a PPR (Points Per Reception) format.  Fantasy football is an industry valued at over $18 billion with over 60 million players in North America.  As such, there is no shortage of individuals looking to get a competitive edge on the friends, family and co-workers they participate with.
<br><br>

## Table of Contents
<br>

Directories
* [Data](https://github.com/bernpb/LHL_Final_Project/tree/master/Data) - Data in .csv format that was used to complete the project.
* [Docs](https://github.com/bernpb/LHL_Final_Project/tree/master/Docs) - Images, progress report, notes
* [Modelling Work](https://github.com/bernpb/LHL_Final_Project/tree/master/Modeling%20Work) - Jupyter and Google Colab notebooks containing my modelling pipelines.
* [Pickles](https://github.com/bernpb/LHL_Final_Project/tree/master/Pickles) - Serialized models ready for deployment

Notebook Files

* [Player EDA](https://github.com/bernpb/LHL_Final_Project/blob/master/EDA.ipynb) - Exploratory data analysis focused on individual player performance
* [Team EDA](https://github.com/bernpb/LHL_Final_Project/blob/master/Team_Performance_EDA.ipynb) - Exploratory data analysis focused on team performance
* [Final Model](https://github.com/bernpb/LHL_Final_Project/blob/master/SVR_Final.ipynb) - Finalized support vector regressor model that I have deployed
* [Data Wrangling](https://github.com/bernpb/LHL_Final_Project/blob/master/Data_wrangling.ipynb) - Notebook focused on data acquisition through API calls and formatting

Python Files

* [Functions](https://github.com/bernpb/LHL_Final_Project/blob/master/Project_Functions.py) - Collection of functions employed in the cleaning, engineering and transformation steps of my machine learning pipelines.
* [Generate Data](https://github.com/bernpb/LHL_Final_Project/blob/master/Generate_Data.py) - Function that builds the data that my model will use to make a player prediction
* [Plotting](https://github.com/bernpb/LHL_Final_Project/blob/master/Make_Plots.py) - Function that makes the plotly plots displayed alongside a prediction on the web app.
* [Streamlit App](https://github.com/bernpb/LHL_Final_Project/blob/master/Deploy.py) - Streamlit web application

## Methods
To tackle this challenge, I sourced the bulk of my data from the [SportsData.io](https://sportsdata.io) and [MySportsFeeds](https://www.mysportsfeeds.com/) APIs as well as [Pro Football Reference](https://www.pro-football-reference.com/).  

As with many sports datasets, this data was heavily right skewed.  Most active players had values at or close to 0 for most stat lines, while top performers (the ones we are focused on in fantasy)
tend to have more extreme values.  As such, a customized log transformation was applied in certain models which resulted in better overall accuracy.  This transformation involved adding a constant to continuous variables to ensure that they were positive and non-zero.  

Most of the features that were engineered relied on past player performance data in order to make predictions about the future.  In most cases, this data was transformed into a set of trailing averages, tracking the player's performance over the last 3 or 7 games.  Using this data, players were also binned into tiers as shown in the graphic below.  Categorical features such as past injury status and opposing team strength were also used in modeling.   

# FIGURE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


As a regression problem the models I employed to tackle the problem were simple linear regression, random forest, SVR, gradient-boosted trees as well as a deep neural network.  As this project is an academic pursuit, I spent some time with each of these techniques to better understand their intricacies.  The model with the best performance was a support vector machines regressor using an RBF kernel. The model was able to predict on my test set with an R2 score of 0.494 and a mean squared error of 28.89.
<br><br>
## Deployment
The model has been deployed using an Amazon EC2 instance with the streamlit library providing the interactive front end.  A link to the web application can be found [here](http://13.58.187.7:8501/).  Using the app, a user can input the name of any active ball-carrier in the NFL and get a prediction of how many fantasy points that player can be expected to accumulate for the given week of the season. 
<br><br>
## Future Work
One of the features that I would like to implement in the future would be to integrate natural language processing into my model.  This application would be two fold:

* Tracking the injury status of a player
    * As of right now, I don't have a method of detecting whether a given player is likely to start the game or not.  As such, I would like to use Twitter's API to get tweets and determine the probability that a player's injury will prevent them from playing in a given game.  
* Sentiment Analysis as a feature
    * Similar to the injury status, I would like to use twitter to get public sentiment about a player going into a game.  My theory here is that roster changes, favorable matchups, etc. can correlate with fantasy performance and would be reflected around the discussion of a player online.
* Acquisition of More Data
    * Getting my hands on more seasons of data as well as more robust statistics (snap count, red zone performance, etc) would likely help to improve my model performance significantly.
    * It would also allow me to model each position with it's own model, which could greatly improve the accuracy of my model going forwards.  