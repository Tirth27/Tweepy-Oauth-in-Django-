from django import forms

# Create your forms here.

class PostTweet(forms.Form):
	input_tweet = forms.CharField()
