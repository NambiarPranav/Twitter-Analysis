# README

##What it does?##

This application gets twitter data related to Arvind Kejrival and Narendra Modi and finds out different features in it like number of original tweets,retweets,tweets with only images etc

##How does it get twitter data?##
It uses twitters streaming api to get the recently tweeted tweets related to the aforementioned people.As twitter limits the amount of data accessible at one time,I used a cronjob on my laptop to run the twitter_data_gatherer again and again to get the data

##How does it work?##
The data_processor file then looks at various data and features recieved and figures out stuff like is the current tweet a retweeted tweet or an original tweet,does the tweet have any image or not,what are the hashtags used in the tweet etc,etc.

##How is it displayed?##
The web application is made on ruby, the data gathered by the data_processor is saved in a text file and then ruby accesses it to display them on the application
