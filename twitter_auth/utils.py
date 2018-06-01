import tweepy

<<<<<<< HEAD
CONSUMER_KEY = 'aUXfolDvlnFvYih0sgsZogXG9'
CONSUMER_SECRET = 'NToS7KtPWUQzGVBgU4kRXml1hY3Rx8JK17bfYeFilxEivTSWEm'
=======
CONSUMER_KEY = 'Enter_your_key'
CONSUMER_SECRET = 'Enter_your_secret'
 
>>>>>>> 6c01f8e1d613d049cf73199a78c9d1339cf9726e

def get_api(request):
	# set up and return a twitter api object
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	access_key = request.session['access_key_tw']
	access_secret = request.session['access_secret_tw']
	oauth.set_access_token(access_key, access_secret)
	api = tweepy.API(oauth)
	return api
