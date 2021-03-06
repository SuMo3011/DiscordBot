import praw
import os
import random
reddit_client = os.environ['reddit_client']
reddit_secret = os.environ['reddit_secret']
reddit_user = os.environ['reddit_user']
reddit_pass = os.environ['reddit_pass']

def create_reddit_object():

  return praw.Reddit(client_id = reddit_client,
  client_secret = reddit_secret, 
  user_agent = 'Discord Bot', 
  username =  reddit_user,
  password = reddit_pass,
  check_for_async=False)


def get_post(reddit_client, subreddit, sort_by, over_18, image = False):
  subred = reddit_client.subreddit(subreddit)
  post_list = []
  image_ext = ['.jpg', '.png', '.jpeg', 'gif']

  if sort_by == 'hot':
    posts = subred.hot(limit=50)

  if sort_by == 'new':
    posts = subred.new(limit=50)

  if sort_by == 'top':
    posts = subred.top(limit=50)

  for post in posts:

    if post.pinned == False and post.over_18 == over_18 and len(post.selftext)<=1500:
      if image:
        if not any(str(post.url).endswith(ext) for ext in image_ext):
          continue
      else:
        if any(post.url.endswith(ext) for ext in image_ext):
          continue
      post_list.append(post)
      
  if len(post_list)==0:
    return "Try Again, no post found"
  return random.choice(post_list)

# reddit = create_reddit_object()
# post = get_post(reddit, 'Jokes', 'hot', False)
# print(post.pinned, post.title)
