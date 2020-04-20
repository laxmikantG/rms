from django import template

register = template.Library()


def calculate_total(value, arg):
    """Removes all values of arg from the given string"""
    print(value, arg)
    return value.replace(arg, '')

register.filter('calculate_total', calculate_total)
