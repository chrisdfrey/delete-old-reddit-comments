from datetime import datetime, timedelta
import praw

# TODO: convert to installed/web app

# need to use your own values for these
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password=""
)

old_time = datetime.now() - timedelta(days=365)
old_time = old_time.timestamp()

# TODO: use after param instead of fetching all new posts every time

while(True):
    print("starting new deletion batch")

    num_deleted = 0
    for comment in reddit.user.me().comments.new(limit=None):
        if (comment.created_utc < old_time):
            print("deleting comment " + comment.id)
            comment.delete()
            num_deleted += 1

    if (num_deleted == 0):
        break

print("finished")
