<!-- ABOUT THE PROJECT -->
## About The Project

*This project was created for fun in learning purposes, never use it on production, it's raw and not tested at all!*

This project collects top 30 comments from the most recent posts in reddit and creates a file with all translations to russian

### Prerequisites

Please install python3 and git according to your system.
```sh
pacman -S git python3
```

### Installation

1. Register Telegram Bot using Bot Father
2. Clone the repo
   ```sh
   git clone git@github.com:neulad/reddit-scrapper.git
   ```
3. Install pip packages
   ```sh
   pip3 install praw
   ```
4. Enter your data in `application.py`
   ```python
    reddit = praw.Reddit(client_id='PUT YOUR CLIENT ID THERE!!!!!!', client_secret='PUT YOUR CLIENT SECRET THERE!!!!', user_agent='PUT YOUR USER AGENT THERE!!!')
    api = "PUT YOU API KEY THERE!!!!!"
   ```

<!-- USAGE EXAMPLES -->
## Usage

Usage is pretty fare, just run

```sh
python3 redditScraper.py
```
