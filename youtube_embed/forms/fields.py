from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug

from widgets import YoutubeVideoWidget

class YoutubeVideoField(forms.CharField):

    # YT IDs only use letters, numbers, underscores and hyphens
    default_validators = [validate_slug]
    widget = YoutubeVideoWidget

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        max_length = 11 if max_length is None else max_length
        min_length = 11 if min_length is None else min_length
        super(YoutubeVideoField, self).__init__(max_length=max_length,
                                                min_length=min_length,
                                                *args, **kwargs)

    def to_python(self, value):
        return super(YoutubeVideoField, self).to_python(value[1])
