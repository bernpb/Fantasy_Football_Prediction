# Day 0
### Thursday, November 14th, 2021

* Created project readme with project description and context
* Set up git repository for project
* Set up new environment for the project
* Set up .gitignore and config.py files to hide secrets
* Confirmed access to data via the sportsdata.io API
* Spoke with Andrew about the potential of using sentiment analysis as feature engineering.  Suggested that it be saved as a stretch goal.
* Downloaded weekly player data via API.  Took ~ 5 hours due to a minimum 5 minute delay between requests.
    * Explored said data, tested requests to make sure that the required data and is available
    
# Day 1
### Friday, November 19th, 2021

* Exploratory Data Analysis Started
    * Impacts of specific stat lines on fantasy production
        * Rushing Yards
        * Touchdowns
        * Checking how well the tiers (bins) I created for positions separate the data
* Explored strategies and functions I can use for feature engineering
    * Figure out how to perform the 3-game rolling average calculation on a per-player basis
    * Assign players to tiers based on the quality of their recent play
        
# Day 2
### Saturday, November 20th, 2021

* Continued Exploratory Data Analysis
    * Created correlation matrix to explore how features I might want to engineer will correlate to target
* Working on strategies for preprocessing data and merging sources
* Get scoring data for each game played
    * Developped a method for mapping scores and team yardage to each observation in the set
    * Will use this to develop a feature representing how much a player contributes to their team's offense
    
# Day 3
### Sunday, November 21st, 2021
 
 * Write a function to assign game points to the correct team.  (Home/Away)
 * Created features describing a player's individual contribution to a team's offense.
 * Expanded EDA
 * Prep for performing a baseline model tomorrow
 
# Day 4
### Monday, November 22nd, 2021
 
 * Implement a pipeline for all feature engineering and preprocessing
 * Investigate large imbalance between players with a score of 0 and players that scored (Turns out to be about 50% of players with a zero score)
 * Built baseline linear regression model
     * Implemented PCA, did not improve the model quality
 * Built a polynomial regression model
 * Built out a Random Forest Model
 
# Day 5
### Tuesday, November 23rd, 2021
 
 * Acquire updated dataset for week 12 of season
 * Squashed bugs.  So many bugs
 * Applied log transform
 * Built out a NN (Google Collab)
 * XGBoost model (Google Collab)
 * Engineer more lagged features
 
# Day 6
### Wednesday, November 24th, 2021
 
 * Squashed bugs.  Fewer than yesterday
 * Applied log transform
 * Parameter tuning which led to a rebuild of neural network
 * Parameter tuning and application of pipeline on XGBoost model
 * Research into streamlit and a few tutorials
 * Back to the EDA
 
 
 # Day 7
 ### Thursday, November 25th, 2021
 
 * Streamlit tutorials and reading documentation
 * Model tuning
 * Work on Streamlit web app
 * Set up Amazon EC2 instance for deployment
 * Generate dataset for prediction
 
 
# Day 8
### Friday, November 26th, 2021
 
 * Completed SVR Modelling (Best one yet)
 * Worked on streamlit web app
 * Dove into EDA of defensive and offensive team performance as feature engineering
 * Developped functions for engineering defensive and offensive features
 * Created two sets of trailing average data, increased model performance across the board.

 
# Day 9
### Saturday, November 27th, 2021

* Developped new features to track overall team metrics
    * Overall offensive scoring
    * Metrics for evaluating the strength of opposing defenses
* Implemented weather as a feature
    * Did not improve the model so it was scrapped
    
# Day 10
### Sunday, November 28th, 2021

* First deployment of model using an Amazon EC2 instance
* Updated visualization candidates for presentation


# Day 11
### Monday, November 29th, 2021

* Code review and refactoring
* Updated streamlit app using st.cache to improve app performance
* Added visualizations to app output
* Work on presentation started
* Updated visualization candidates for presentation

# Day 12
### Tuesday, November 30th, 2021

* Visualizations for presentation
* Final deployment of model
* Updated project readme and created a table of contents for github
* Presentation

# Day 13
### Wednesday, December 1st, 2021

* Tweaks to presentation
* Presentation run-throughs
* Got the defensive strength feature working
* Notebook cleanup