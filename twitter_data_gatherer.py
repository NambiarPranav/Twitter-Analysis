import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import io

from pymongo import MongoClient
import json
from pprint import pprint

#insert the 4 keys you get from twitter
ckey = '#'
consumer_secret = '#'
access_token_key = '#'
access_token_secret = '#'


start_time = time.time() 
#list of keywords to search from twitter 
keyword_list = ['kejriwal','modi'] 





 
#listens and grabs data from twitter
class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
	 
		self.time = start_time
		self.limit = time_limit
		 
	def on_data(self, data):
	 
		while (time.time() - self.time) < self.limit:
		 
			try:		 
				client = MongoClient('localhost', 27017)
				db = client['twitter_db']
				collection = db['twitter_collection']
				tweet = json.loads(data)				 
				collection.insert(tweet)
				 
				return True
				 
			 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
				 
		exit()
	 
	def on_error(self, status):
		print statuses




def main():
	auth = OAuthHandler(ckey, consumer_secret) #OAuth object
	auth.set_access_token(access_token_key, access_token_secret)
	 
	 
	twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
	try:
		twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method
	except Exception,e:
		print e
		twitterStream.disconnect()

if __name__=="__main__":
	main()

