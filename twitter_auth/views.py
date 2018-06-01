
import tweepy
from django.http import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib import messages

from django.shortcuts import render
import re #import regular expression
from twitter_auth.forms import PostTweet #import form

from twitter_auth.utils import *
from profanityfilter import ProfanityFilter #it's a library for detecting proform word in any given list

pf = ProfanityFilter()

def main(request):
	"""
	main view of app, either login page or info page
	"""
	# if we haven't authorised yet, direct to login page
	if check_key(request):
		return HttpResponseRedirect(reverse('info')) #goto info
	else:
		return render_to_response('twitter_auth/login.html') #goto login

def unauth(request):
	"""
	logout and remove all session data
	"""
	if check_key(request):
		api = get_api(request)
		request.session.clear()
		logout(request)
	return HttpResponseRedirect(reverse('main'))

def info(request):
	"""
	display some user info to show we have authenticated successfully
	"""
	print(check_key)
	if check_key(request):
		api = get_api(request)
		user = api.me()
		return render_to_response('twitter_auth/info.html', {'user' : user})
	else:
		return HttpResponseRedirect(reverse('main'))

def auth(request):
	# start the OAuth process, set up a handler with our details
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	# direct the user to the authentication url
	# if user is logged-in and authorized then transparently goto the callback URL
	auth_url = oauth.get_authorization_url(True)
	response = HttpResponseRedirect(auth_url)
	# store the request token
	request.session['request_token'] = oauth.request_token
	return response

def callback(request):
	verifier = request.GET.get('oauth_verifier')
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	token = request.session.get('request_token')
	# remove the request token now we don't need it
	request.session.delete('request_token')
	oauth.request_token = token
	# get the access token and store
	try:
		oauth.get_access_token(verifier)
	except tweepy.TweepError:
		print('Error, failed to get access token')

	request.session['access_key_tw'] = oauth.access_token
	request.session['access_secret_tw'] = oauth.access_token_secret
	print(request.session['access_key_tw'])
	print(request.session['access_secret_tw'])
	response = HttpResponseRedirect(reverse('info'))
	return response

def check_key(request):
	"""
	Check to see if we already have an access_key stored, if we do then we have already gone through
	OAuth. If not then we haven't and we probably need to.
	"""
	try:
		access_key = request.session.get('access_key_tw', None)
		if not access_key:
			return False
	except KeyError:
		return False
	return True


#read tweet from home_timeline
def home_timeline(request):
    if check_key(request):
    	api = get_api(request)
    	public_tweets = api.home_timeline()

    	return render(request, 'twitter_auth/public_tweets.html', {'public_tweets': public_tweets})
    else:
        return render_to_response('twitter_auth/login.html') #goto login

#post tweet    
def post_tweet(request):
   tweet = "not logged in"
   if check_key(request):
       	if request.method == "POST":
              #Get the posted form
              MyPostTweet = PostTweet(request.POST)
              if MyPostTweet.is_valid():
                #get user input
                tweet = request.POST.get("input_tweet", "")
                Approval=pf.is_profane(tweet)
                 #applying profanity for explicit content detection
                 #it won't allow post any explicit tweets
                if Approval == True:
                  messages.success(request, "Explicit Contect detected !")
                  messages.success(request, "Please try again.")
                else :
                  messages.success(request, "Neat and clean !")
                  messages.success(request, "Status Updating...")
                  api = get_api(request)
                  #update status
                  api.update_status(tweet)
       	else:
          		MyPostTweet = PostTweet()
		
        return render(request, 'twitter_auth/post_tweet.html', {"tweet" : tweet})
    
   else:
        return render_to_response('twitter_auth/login.html') #goto login
    
