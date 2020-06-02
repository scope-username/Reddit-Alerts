import praw
import sendgrid
from sendgrid.helpers.mail import *
import schedule
import time

# Reddit env variables
reddit_client_id = {}
reddit_client_secret = {}
reddit_user_agent = {}
reddit_username = {}
reddit_password = {}

myReddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent,
                       username=reddit_username, password=reddit_password)

# SendGrid env variables
sendgrid_from = {}
sendgrid_api_key = {}
email_recipients = ['my@email.com', 'myfriend@email.com']

# Subreddit list that you want to search in
mySubreddits = ['buildapcsales', 'gamedeals', 'pcmasterrace', 'techdeals']

# Tags that you are looking for
myTags = ['cpu', 'prebuilt', 'mouse', 'keyboard']


def send_email(email_content):
    message = Mail(
        from_email=sendgrid_from,
        to_emails=email_recipients,
        subject='Reddit Alerts from Python',
        html_content=email_content)
    try:
        sg = sendgrid.SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print("send grid response code", response.status_code)
    except Exception as e:
        print(e)


def upvote_post(post_id):
    post = myReddit.submission(id=post_id)
    post.upvote()


def job():
    email_content = ""
    for mySubreddit in mySubreddits:
        for submission in myReddit.subreddit(mySubreddit).new(limit=20):
            if any(myTag in (submission.title or submission.selftext) for myTag in myTags):
                if submission.likes is None:
                    print(submission.title, submission.shortlink)
                    email_content += "<b>Title</b> : " + submission.title + " <b>Link</b> : " + submission.shortlink +"<br>"
                    upvote_post(submission.id)
    send_email(email_content)


# job()
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
