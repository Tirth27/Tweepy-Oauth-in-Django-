import tweepy

CONSUMER_KEY = 'kHPHMnOrnNTId2usSTlH3Gx6l'
CONSUMER_SECRET = 'xm6KqejBPZeuqaUK2fq5bufKX5PeDXnzkMEHPdxCH1TtKXFIp3'
 

def get_api(request):
	# set up and return a twitter api object
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	access_key = request.session['access_key_tw']
	access_secret = request.session['access_secret_tw']
	oauth.set_access_token(access_key, access_secret)
	api = tweepy.API(oauth)
	return api
