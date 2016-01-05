# coding: utf-8

from django import template

register = template.Library()


@register.filter(name='test')
def test(value):
    """
       test
    """
    return value + " test"
