#pip install python-instagram
client_id = '1f1f1f1713664ee48432208f96e297d9'
client_secret = '2c2973d5f3884ca2846c1ff24adfe22b'
access_token = '8426282018.1f1f1f1.c974e3077dcf4667a7b99f8fb6df4b0d'
user_id = 'basterfluit'
from instagram.client import InstagramAPI

# api = InstagramAPI(access_token=access_token, client_secret=client_secret)
#
# result = api.user_recent_media(user_id=user_id, count=10)
# print(result)
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
#api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print(media.images['standard_resolution'].url)
