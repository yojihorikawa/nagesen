import tweepy
from twstreamlistener import TwStreamListener

# need to adjust the time otherwise it returns 401
# apk --update add tzdata && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && apk del tzdata && rm -rf /var/cache/apk/*
# docker run --rm --privileged alpine hwclock -s


Consumer_key = ''
Consumer_secret = ''
Access_token = ''
Access_secret = ''

try:
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)

    twStreamListener = TwStreamListener(api)
    twStream = tweepy.Stream(auth = api.auth, listener=twStreamListener)
    twStream.filter(track=['@hogehogepu'])
except Exception as e:
    print(e)
