from __future__ import unicode_literals
from django import template

register = template.Library()

@register.simple_tag
def render_title_span_for(bound_field):
    return '<span id="title_{0}"></span>'.format(bound_field.id_for_label)

@register.simple_tag
def render_img_for(bound_field):
    return '<img id="img_{0}" src="" />'.format(bound_field.id_for_label)

@register.simple_tag
def render_desc_span_for(bound_field):
    return '<span id="desc_{0}"></span>'.format(bound_field.id_for_label)

def player_for(video_id, **kwargs):
    height = kwargs.get('width', '390')
    width = kwargs.get('width', '640')
    return {'video_id': video_id, 'width': width, 'height': height}

register.inclusion_tag('youtube_embed/player_full.html', name='full_player_for')\
                      (player_for)
register.inclusion_tag('youtube_embed/player_lite.html', name='lite_player_for')\
                      (player_for)
