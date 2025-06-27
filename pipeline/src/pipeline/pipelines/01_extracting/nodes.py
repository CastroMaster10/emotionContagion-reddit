import praw
import os
import dotenv
import json
import time


dotenv.load_dotenv()



def extract_comments_replies(submission: object) -> json:

    submission.comments.replace_more(limit=100)
    comment_tree = {}
    for comment in submission.comments:
        comment_tree[comment.id] = {
            "body": comment.body,
            "replies": [reply.body for reply in comment.replies]
        }
    return comment_tree



def extract_submissions(subreddit: object,limit_requests: int) -> dict:

    submissions = {}
    for submission in subreddit.hot(limit=limit_requests):
        submissions[submission.id] =  {
            "author": submission.author_flair_text,
            "url": submission.url,
            "num_comments": submission.num_comments,
            "title": submission.title,
            "comments":  extract_comments_replies(submission)
        }




    return submissions




def extract_subreddits(limit_requests: int=10) -> json:

    """
    Extracts data from Reddit using PRAW and returns it as a DataFrame.
    Args:
        limit_requests (int): The number of requests to limit the extraction to.
    Returns:    pd.DataFrame: A DataFrame containing the extracted data."""

    reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    password=os.getenv("MY_PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
    username=os.getenv("MY_USERNAME"),
    ratelimit_seconds = 60
    )



    subreddit = reddit.subreddit("politics")


    payload = {
        "id":subreddit.id,
        "subreddit_name": subreddit.display_name,
        "description": subreddit.public_description,
        "posts":  extract_submissions(subreddit,limit_requests)
    }





    return payload

