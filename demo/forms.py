from django import forms

from youtube_embed.forms.fields import YoutubeVideoField

class WidgetTest(forms.Form):
    youtube_id = YoutubeVideoField()

