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
