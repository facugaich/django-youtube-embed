from django import forms

from youtube_embed.forms.fields import YoutubeVideoField

from models import ModelTest

class WidgetTest(forms.Form):
    youtube_id = YoutubeVideoField()

class ModelTestForm(forms.ModelForm):
    youtube_id = YoutubeVideoField()
    class Meta:
        model = ModelTest
