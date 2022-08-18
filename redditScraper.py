from praw.models import MoreComments
import requests
import praw

reddit = praw.Reddit(client_id='PUT YOUR CLIENT ID THERE!!!!!!', client_secret='PUT YOUR CLIENT SECRET THERE!!!!', user_agent='PUT YOUR USER AGENT THERE!!!')
api = "PUT YOU API KEY THERE!!!!!"

comments = reddit.submission(url="https://www.reddit.com/r/AskReddit/comments/esy81b/"
	                             "what_is_a_one_in_a_million_thing_that_happend_to/").comments
comments.replace_more(limit=0)

with open("en-ruComments.txt", "w") as f:
	f.write("")
	for i in range(30):
		enText = str(comments[i].body)
		print(i)
		ruText = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}".format(api, 
			enText, "en-ru").replace("#", "")).json()["text"][0]
		f.write(str(i + 1) + ".\n\n" + "English:\n\n" + enText + "\n\n" + "Russian:\n\n" + ruText + "\n\n")
