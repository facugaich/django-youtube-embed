from __future__ import unicode_literals
from django.forms.widgets import MultiWidget, HiddenInput, TextInput

class YoutubeVideoWidget(MultiWidget):

    hook_class = 'youtube-embed-container'
    canonic_url = 'http://www.youtube.com/watch?v={0}'

    def __init__(self, attrs=None):
        widgets = (TextInput, HiddenInput)
        super(YoutubeVideoWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [self.canonic_url.format(value), value]
        return [None, None]

    def format_output(self, rendered_widgets):
        output = '<span class="{0}">'.format(self.hook_class) +\
                 ''.join(rendered_widgets) +\
                 '</span>'
        return output

    class Media:
        js = ('youtube-embed.js',)
