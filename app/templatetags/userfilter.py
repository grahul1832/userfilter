from django import template
register = template.Library()


def swap(data):
    return data.swapcase()

register.filter('swap',swap) 