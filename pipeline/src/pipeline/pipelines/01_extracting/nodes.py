import praw
import os
import dotenv
import pandas as pd

dotenv.load_dotenv()


def extract_comments(subreddit_name: str, limit_requests: int) -> pd.DataFrame:

    pass

def extract_subreddits(limit_requests: int) -> list:

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
    )

    df = pd.DataFrame(columns=["title", "score", "id", "url", "comments"])


    subreddits = reddit.subreddits.popular(limit=limit_requests)

    names = []
    for submission in subreddits:
        names.append(submission.display_name)

    return names


print(extract_subreddits(100))  # Example usage, replace with actual subreddit name

