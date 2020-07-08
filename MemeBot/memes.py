import praw
import credentials

reddit = praw.Reddit(client_id=credentials.client_id,
                     client_secret=credentials.client_secret, password=credentials.password,
                     user_agent=credentials.user_agent, username=credentials.username)

def gather_meme():
	subreddits=['dankmemes','funny','meme','memes','HistoryMemes','Animemes','HolUp','PrequelMemes']
	#subreddits=['dankmemes']

	info_list=[]

	for subreddit in subreddits:
		try:
			subreddit=reddit.subreddit(subreddit)
			top_sub = subreddit.top('hour',limit=6)
			for submission in top_sub:
				if not submission.stickied:
					info_list.append([subreddit,submission.author,submission.url])

		except praw.exceptions.PRAWException as e:
			pass

	return info_list