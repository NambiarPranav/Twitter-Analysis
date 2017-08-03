from pymongo import MongoClient
import json
import operator
 

#Used to get the collection data from the mongodatabase
client = MongoClient('localhost', 27017)
db = client['twitter_db']
collection = db['twitter_collection']
cursor=collection.find({})

#Used to count a bunch of stuffs
count_text=0
count_image=0
count_both=0
count_retweeted=0
count_tweets=0
counthashtag=0
flag=0
count_favorite=0
count_kejrifam=0
count_modifam=0

#All the tweets used with their corresponding frequency
tweets_dict={}

#Calculating all the values
for document in cursor:
	#To calulate how famous modi and kejriwal are in delhi
	if "user" in document.keys():
		us=document["user"]
		if "location" in us.keys():
			loca= (us["location"])
			if (type(loca)==unicode):
				loca=loca.lower()
				if "delhi" in loca:
					stri=(document["text"])
					tex=stri.encode('utf8')
					tex=tex.lower()
					# print (tex)
					if "kejriwal" in tex:
						count_kejrifam=count_kejrifam+1
					else:
						count_modifam=count_modifam+1
					# print (loca)
	#Check if the current tweet is retweeted or original
	if "retweeted_status" in document.keys():
		count_retweeted=count_retweeted+1
	else:
		#If original check the favorite count
		if "favorite_count" in document.keys():
			count_favorite=count_favorite+document["favorite_count"]
	flag=0
	count_tweets=count_tweets+1
	# Insert the hashtags into the dictionary
	if "text" in document:
		stri=(document["text"])
		tex=stri.encode('utf8')
		texti=tex
		tex=tex.split(" ")
		for word in tex:
			if "#" in word:
				word=word.split("#")
				ct=0
				for wrd in word:
					if (ct>0):
						counthashtag=counthashtag+1
						if wrd in tweets_dict.keys():
							tweets_dict[wrd]=tweets_dict[wrd]+1
						else:
							tweets_dict[wrd]=1
					ct=ct+1
		loci=loc=len(texti)
		if "#" in texti:
			loc=texti.index("#")
			texti=texti[:loc]
		if (len(texti)>30):
			count_text=count_text+1
			flag=1
	thestr=str(document)
	#Check if there is any image in the file
	if "media" in thestr:
		if (flag==0):
			count_image=count_image+1
		else:
			count_text=count_text-1
			count_both=count_both+1
# Write all the data to text file
f=open("/home/pranav/Desktop/TweetDisplayer/myfile.txt",'w')
f.write (str(count_image)+"\n")
f.write (str(count_text)+"\n")
f.write (str(count_both)+"\n")
f.write (str(count_retweeted)+"\n")
f.write (str(count_tweets)+"\n")
f.write (str(counthashtag)+"\n")
f.write (str(count_favorite)+"\n")
f.write (str(count_modifam)+"\n")
f.write (str(count_kejrifam)+"\n")
# SOrt the tweets dictionary in ascending order
sorted_tweets_dict_keys=sorted(tweets_dict.items(),key=operator.itemgetter(1))
no_of_tweets=len(sorted_tweets_dict_keys)
i=1
while (i<12):
	f.write (sorted_tweets_dict_keys[no_of_tweets-i][0]+"\n")
	i=i+1
f.close()

