
from twitter_setup import api
result = api.users.lookup( user_id  = 3158756977 )

print(result[0]['screen_name'])
#116787186
