from praw.models import MoreComments
import requests
import praw

reddit = praw.Reddit(client_id='Wur7iJclY-HMXw', client_secret='odD_G7Ew-QEX6nLk_E7soYHBR3g', user_agent='test-app')
api = "trnsl.1.1.20200208T132702Z.4f9e0c4b9ed0583d.2ffb26e53c8f6dc400ef4fcd06f1675f71433dbe"

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
