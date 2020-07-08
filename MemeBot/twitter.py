from twython import Twython, TwythonError
from io import BytesIO
import requests
import urllib
from time import sleep
import credentials
from memes import gather_meme

interval=60*60*2
tweet=Twython(
	credentials.API_Key,
	credentials.API_Secret,
	credentials.Access_token,
	credentials.Access_token_secret
	)

# results=tweet.search(q="#india",count=4)

# all_tweets=results['statuses']

# for tweets in all_tweets:
# 	print(tweets['text'])

while True: #remove this when using locally
	data=gather_meme()

	for i in range(len(data)):
		url=data[i][2]
		author=data[i][1]
		subbreddit=data[i][0]


		response = requests.get(url)
		photo = BytesIO(response.content)

		try:
			response = tweet.upload_media(media=photo)
			MyStatus='by '+str(author)+" #meme #funny #bot #"+str(subbreddit)
			tweet.update_status(status=MyStatus, media_ids=[response['media_id']])
		except:
			pass
		#print(str(i)+' done')
		sleep(15)

	sleep(interval)