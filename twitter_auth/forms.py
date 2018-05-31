from django import forms

# Create your tests here.

class PostTweet(forms.Form):
	input_tweet = forms.CharField()
