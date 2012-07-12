from django import forms

from youtube_embed.forms.widgets import YoutubeVideoWidget

class WidgetTestField(forms.CharField):

    def to_python(self, value):
        return super(WidgetTestField, self).to_python(value[1])


class WidgetTest(forms.Form):
    youtube_id = WidgetTestField(widget=YoutubeVideoWidget())

