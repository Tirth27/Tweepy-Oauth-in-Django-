# Tweepy-Oauth-in-Django
Twitter  authentication using Tweepy and can Post and see HomeTimeline tweets using Django.

Extending the concept of our [Curse-Word-Detection-For-Twitter](https://github.com/PatrioticParth/Curse-Word-Detection-For-Twitter) repository you can see the homeline tweets and can post tweets.
## Install Dependencies
```
pip install tweepy
pip install Django==1.9
```
#### Generate your Twitter Credential if you dont have one from [Twitter Application Manager](https://apps.twitter.com/)
#### Set the Callback URLs in Seting of [Twitter Application Manager](https://apps.twitter.com/) to 
> http://127.0.0.1:8000/callback/

## How To Use
1. Clone the repository
```
git clone https://github.com/Tirth27/Tweepy-Oauth-in-Django-.git
```
3. Run the django server on localhost
```
python manage.py runserver
```
   - You will see the homepage in the you browser![alt text](https://github.com/Tirth27/Tweepy-Oauth-in-Django-/blob/master/images/home.png)


Implementing the Curse word detection in Django.

Ready to use just put your Twitter credential in  Tweepy-Oauth-in-Django-/twitter_auth/utils.py

If you dont have one generate it form https://apps.twitter.com/


