#-------------------------------------------------------------------------------
# Name:        Twitter Setup
# Purpose:     Big Data Twitter Research. This module
#               contains the information to access twitters database.
# Author:      Nikki Sigurdson
# Created:     29/03/2015
#-------------------------------------------------------------------------------

#twitter_setup.py
import twitter

#access tokens

C_KEY = "dKH7YuqkMcioFfLJb0CB8hqa6"
C_SECRET = "leYZLYLp5kYxjXhmeXwQ6CqOgcyvdflXacW6T1Xk0cR8mCB4jQ"
A_TOKEN = "3082354349-8FOJz38gREAyptbztdVo1o4wRPsZtAAAkFQ9tVO"
A_SECRET = "GIVEuguxnn8xJUnogcxkbVYVZeNi0lVi2INlVffTbmBUW"
'''
# CLASS CODE BELOW

# instantiate the OAuthhandler
auth = twitter.oauth.Oauth(A_TOKEN, A_SECRET,C_KEY,C_SECRET)

#INSTANTIATE THE TWITTER OBJECT.
api = twitter.Twitter(auth=auth)
'''

api = twitter.Twitter( auth = twitter.oauth.OAuth(A_TOKEN, A_SECRET,C_KEY,C_SECRET))

#note: this above works, but the original code from class doesnt somehow,
# even though they should be identical?

#other code that doesnt work

'''
import twitter
api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')

import twitter
from twitter import Twitter
  # ...
twitter = Twitter(auth = OAuth(A_TOKEN, A_SECRET, C_SECRET, C_KEY))

# Get the public timeline
twitter.statuses.public_timeline()

'''




