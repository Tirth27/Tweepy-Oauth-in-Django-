# Tweepy-Oauth-in-Django
Twitter authentication using Tweepy API and can Post and see HomeTimeline tweets using Django.

Extending the concept of our [Curse-Word-Detection-For-Twitter](https://github.com/PatrioticParth/Curse-Word-Detection-For-Twitter) repository you can see the homeline tweets and can post tweets.
## Install Dependencies
```
pip install tweepy
pip install Django==1.9
pip install profanityfilter
```
#### Generate your Twitter Credential if you dont have one from [Twitter Application Manager](https://apps.twitter.com/), And Set the Callback URLs in Settings of [Twitter Application Manager](https://apps.twitter.com/) to 
> http://127.0.0.1:8000/callback/

## How To Use
1. Clone the repository
```
git clone https://github.com/Tirth27/Tweepy-Oauth-in-Django-.git
```
2. Generate your **CONSUMER_KEY** and **CONSUMER_SECRET** form [Twitter Application Manager](https://apps.twitter.com/) found under **Keys and Access Tokens** section. And paste the **CONSUMER_KEY** and **CONSUMER_SECRET** in [util.py]( Tweepy-Oauth-in-Django-/twitter_auth/utils.py )
 
3. Run the django server on localhost
```
python manage.py runserver
```
> You will see the homepage in the you browser![alt text](https://github.com/Tirth27/Tweepy-Oauth-in-Django-/blob/master/images/home.png)
   
> Clicking on *Sign in with Twitter* will take you to twitter authentication page to authorize app![alt text](https://github.com/Tirth27/Tweepy-Oauth-in-Django-/blob/master/images/auth_screen_ifnotauth.png)

> Once you have authorize you app it will redirect you *Info* page on your localhost![alt text](https://github.com/Tirth27/Tweepy-Oauth-in-Django-/blob/master/images/info.png)

> Clicking on *Goto to Timeline* will fetch your Hometimeline tweets![alt text](https://github.com/Tirth27/Tweepy-Oauth-in-Django-/blob/master/images/timeline.png)

> Clicking on *Goto to Post* will take you to *post_tweet* page where you can post tweets.
###### Here we have apply the [Profanity-Filter](https://github.com/areebbeigh/profanityfilter) which does not allow user to use profane words in the tweet. If user tries to use the profane words in the tweet, it won't allow user to post the tweet on twitter and shows *Explicit Contect detected ! Please try again.* error message. 
![alt text](https://github.com/Tirth27/Tweepy-Oauth-in-Django-/blob/master/images/tweet.png) 

## Next Steps
1. Rather then using the [Profanity-Filter](https://github.com/areebbeigh/profanityfilter) use the [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) to detect Explicit or Profane words in tweets.

2. Display the *HomeTimeline* tweets in more readable way with the user name, user profile image and user tweets

3. Perform the [Sentiment Analysis](https://github.com/Tirth27/twitter_sentiment_challenge) on each tweets using [TextBlob](https://textblob.readthedocs.io/en/dev/). The label should be either 'Positive' or 'Negative'. You can define the sentiment polarity threshold yourself, whatever you think constitutes a tweet being positive/negative. And display tweets with its polarity in the HomeTimeline page.

## Credits

The credit for this project goes to @github/Tirth27  and @github/PatrioticParth


