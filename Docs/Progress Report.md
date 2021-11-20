# Day 0
### Thursday, November 14th, 2021

* Created project readme with project description and context
* Set up git repository for project
* Set up new environment for the project
* Set up .gitignore and config.py files to hide secrets
* Confirmed access to data via the sportsdata.io API
* Spoke with Andrew about the potential of using sentiment analysis as feature engineering.  Suggested that it be saved as a stretch goal.
* Downloaded data via API.  Took ~ 5 hours due to a minimum 5 minute delay between requests.
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
        
